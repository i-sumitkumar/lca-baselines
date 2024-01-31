import dataclasses
import json
import os.path
from typing import Dict, List, Any, Optional, Callable
from dataclasses import dataclass
import torch
from datasets import load_dataset
from joblib import Parallel, delayed
from tqdm.auto import tqdm
import multiprocessing

from code_completion.data_classes.datapoint_base import DatapointBase
from code_completion.data_classes.datapoint_commit_dataset import DatapointCommitDataset


@dataclass
class TokenizerOutput:
    context: List[int]
    completion: List[int]


class PreprocessorBase:
    def __init__(self,
                 filepath: str,
                 tokenizer_path: str | None = None,
                 context_composer: Callable[[Dict[str, Any]], str] | None = None,
                 completion_composer: Callable[[Dict[str, Any]], str] | None = None,
                 data_source: str = 'hf',
                 ):
        self.filepath = filepath
        self.data: list[DatapointBase] = self._load_data(filepath)
        self.prepared_data: Optional[List[Dict[str, Any]]] = None
        self.tokenizer_path = tokenizer_path
        self.context_composer = context_composer
        self.completion_composer = completion_composer
        self.data_source = data_source

    def compose_context(self, context: Dict[str, str]) -> str:
        raise NotImplementedError

    def compose_completion(self, context: Dict[str, str]) -> str:
        raise NotImplementedError

    def prepare_data(self):
        print('Data Preparation...')
        self.prepared_data = list()
        for datapoint in tqdm(self.data):
            new_datapoint = dict()
            new_datapoint['repo_id'] = datapoint.repo_id
            new_datapoint['repo_name'] = datapoint.repo_name
            new_datapoint['completion_lines'] = datapoint.completion_lines

            if self.context_composer is None:
                new_datapoint['context'] = self.compose_context(datapoint)
            else:
                new_datapoint['context'] = self.context_composer(datapoint)
            if self.completion_composer is None:
                new_datapoint['completion'] = self.compose_completion(datapoint)
            else:
                new_datapoint['completion'] = self.completion_composer(datapoint)

            # Following fields must be filled after tokenization
            new_datapoint['context_len'] = None  # number of tokens in `context`
            new_datapoint['model_input'] = None  # tokenized `context` + tokenized `completion`
            # new_datapoint['common_api'] = common_api
            self.prepared_data.append(type(datapoint)(**new_datapoint))

    def _datapoint_to_model_input(self, datapoint: DatapointBase) -> DatapointBase:
        datapoint = datapoint.to_model_input(self.tokenize_datapoint)
        return datapoint

    def prepare_model_input_parallel(self, num_workers=None, dataset_path=None):
        self.prepare_data()
        if num_workers is None:
            num_workers = multiprocessing.cpu_count()

        if os.path.exists(dataset_path):
            os.remove(dataset_path)

        with Parallel(num_workers) as pool:
            result = pool(delayed(self._datapoint_to_model_input)(datapoint) for datapoint in self.prepared_data)

        list_to_save = list()
        print('Tokenization...')
        for p in tqdm(result):
            list_to_save.append(dataclasses.asdict(p))

        with open(dataset_path, 'w') as json_file:
            json.dump(list_to_save, json_file)


    def tokenize(self, text) -> List[int]:
        raise NotImplementedError

    def tokenize_datapoint(self, datapoint: DatapointBase) -> TokenizerOutput:
        # print(len(datapoint.context), len(datapoint.completion))
        cropped_context = datapoint.context[-500_000:]  # TODO: connect this to max_seq_len
        return TokenizerOutput(
            context=self.tokenize(cropped_context),
            completion=self.tokenize(datapoint.completion)
        )

    def save_model_inputs(self, filepath='lca/code_generation/data/model_inputs.json'):
        with open(filepath, 'w') as f:
            json.dump(self.prepared_data, f)

    def _load_data(self, path: str) -> list[DatapointBase]:
        if True: #self.data_source == 'hf':
            data = list()
            hf_data = load_dataset(path, split='test')
            repos_list = list(set([hf_dp['repo'] for hf_dp in hf_data]))
            repos_map = {repo: repo_num for repo_num, repo in enumerate(repos_list)}

            for hf_dp in hf_data:
                dp = dict()
                dp['repo_name'] = hf_dp['repo']
                dp['repo_id'] = repos_map[hf_dp['repo']]
                dp['completion_lines'] = hf_dp['completion_lines']
                # dp['completion_lines_raw'] = hf_dp['completion_lines_raw']
                filenames, contents = hf_dp['repo_snapshot']['filename'], hf_dp['repo_snapshot']['content']
                assert len(filenames) == len(contents)
                dp['context_dict'] = {filename: content for filename, content in zip(filenames, contents)}
                # dp['context_dict'] = {el['filename']: el['content'] for el in hf_dp['repo_snapshot']}
                dp['completion_dict'] = {hf_dp['completion_file']['filename']: hf_dp['completion_file']['content']}
                data.append(DatapointCommitDataset(**dp))

            return data

        # with open(path, 'r') as f:
        #     data = json.load(f)
        # return data


import youtokentome as yttm
class FLPythonPreprocessor(PreprocessorBase):
    def __init__(self, filepath, tokenizer_path=None, **composers):
        super().__init__(filepath, tokenizer_path, **composers)
        self.lang_sep_symbol = '₣'
        self.meta_info_sep_symbol = '𐌼'
        self.extension = '.py'
        self._tokenizer: yttm.BPE

    def compose_context(self, datapoint: DatapointBase) -> str:
        context = datapoint.context_dict
        repo_name = datapoint.repo_name
        # You could implement specific order of contents in composed_content
        composed_content = [path + self.meta_info_sep_symbol + content for path, content in context.items()]
        repo_metainfo = f"{self.extension}{self.lang_sep_symbol}{repo_name}{self.meta_info_sep_symbol}"
        return repo_metainfo + self.lang_sep_symbol.join(composed_content)

    def compose_completion(self, datapoint: DatapointBase) -> str:
        completion = datapoint.completion_dict
        # TODO: move path to the context
        composed_content = [path + self.meta_info_sep_symbol + content for path, content in completion.items()]
        return self.lang_sep_symbol + self.lang_sep_symbol.join(composed_content)

    def tokenize(self, text) -> List[int]:
        self._load_tokenizer(self.tokenizer_path)
        if "gpt" in self.tokenizer_path:
            return self._tokenizer(text)['input_ids']
        else:
            return self._tokenizer.encode([text], bos=False, eos=False, dropout_prob=0.0)[0]


    def _load_tokenizer(self, path):
        if "gpt" in path:
            from transformers import GPT2Tokenizer
            self._tokenizer = GPT2Tokenizer.from_pretrained(path)
        else:
            self._tokenizer = yttm.BPE(path)


from transformers import AutoTokenizer
class HFPreprocessor(PreprocessorBase):
    def __init__(self, filepath, tokenizer_path, **composers):
        super().__init__(filepath, tokenizer_path, **composers)
        self.lang_sep_symbol = ''
        self.meta_info_sep_symbol = 'METASEP'
        self.extension = ''
        self._tokenizer: AutoTokenizer

    def compose_context(self, datapoint: DatapointBase) -> str:
        context = datapoint.context_dict
        repo_name = datapoint.repo_name
        # You could implement specific order of contents in composed_content
        composed_content = [path + self.meta_info_sep_symbol + content for path, content in context.items()]
        repo_metainfo = f"{self.extension}{self.lang_sep_symbol}{repo_name}{self.meta_info_sep_symbol}"
        return repo_metainfo + self.lang_sep_symbol.join(composed_content)

    def compose_completion(self, datapoint: DatapointBase) -> str:
        completion = datapoint.completion_dict
        # TODO: move path to the context
        composed_content = [path + self.meta_info_sep_symbol + content for path, content in completion.items()]
        return self.lang_sep_symbol + self.lang_sep_symbol.join(composed_content)

    def tokenize(self, text) -> List[int]:
        self._load_tokenizer(self.tokenizer_path)
        return self._tokenizer(text)['input_ids']

    def _load_tokenizer(self, path):
        self._tokenizer = AutoTokenizer.from_pretrained(path, trust_remote_code=True)


class StarcoderPreprocessor(HFPreprocessor):
    def __init__(self, filepath, tokenizer_path="bigcode/starcoder", **composers):
        super().__init__(filepath, tokenizer_path, **composers)
        self.lang_sep_symbol = 'LANGSEP'
        self.meta_info_sep_symbol = 'METASEP'
        self.extension = '.py'
        self._tokenizer: AutoTokenizer
