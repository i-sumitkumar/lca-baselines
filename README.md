# 🏟️ Long Code Arena Baselines

## What is Long Code Arena? 

[**Long Code Arena**](https://huggingface.co/spaces/JetBrains-Research/long-code-arena) is a suite of benchmarks for code-related tasks with large contexts, up to a whole code repository.
It currently spans six different tasks and contains six datasets:
* 🤗 [Library-based code generation](https://huggingface.co/datasets/JetBrains-Research/lca-library-based-code-generation)
* 🤗 [CI builds repair](https://huggingface.co/datasets/JetBrains-Research/lca-ci-builds-repair)
* 🤗 [Project-level code completion](https://huggingface.co/datasets/JetBrains-Research/lca-project-level-code-completion)
* 🤗 [Commit message generation](https://huggingface.co/datasets/JetBrains-Research/lca-commit-message-generation)
* 🤗 [Bug localization](https://huggingface.co/datasets/JetBrains-Research/lca-bug-localization)
* 🤗 [Module summarization](https://huggingface.co/datasets/JetBrains-Research/lca-module-summarization)

## Where are the baselines? 

For each task, we have different approaches and environments. You can find the baseline solutions and the necessary information about each task in the corresponding directories. 

## How can I submit my results? 

We are excited to invite you to participate in solving our [benchmarks]((https://huggingface.co/spaces/JetBrains-Research/long-code-arena))! To submit your results, please send the following materials to our 📩 email (lca@jetbrains.com):  
* **Results**: Include the summary of your benchmark outcomes.
* **Reproduction Package**: To ensure the integrity and reproducibility of your results, please include the code for context collection (if any), generation of predictions, and evaluating. You can follow [our baselines](https://github.com/JetBrains-Research/lca-baselines) as a reference.  
* **Metadata**: Model information, organization name, licence of your model, context size, and other information you find relevant.

*--------------------------------------------------------------------------------------------------------------*
Steps after clone this repo

add github token in config  then 
in pycharm or ide
Check if the virtual environment was properly created:

Navigate to your project directory (C:\Users\isumi\PycharmProjects\lca-baselines) and make sure that the .venv folder exists.
If the .venv folder does not exist or is incomplete, you can recreate the virtual environment:
bash
Copy code
python -m venv .venv
Activate the virtual environment:

Before running your benchmark, make sure the virtual environment is activated: On Windows, use:
bash
Copy code
.\.venv\Scripts\activate
Install the required dependencies:

After activating the environment, install the project dependencies. Typically, this is done using:
bash
Copy code
pip install -r requirements.txt
Check the path to Python in PyCharm:

In PyCharm, ensure that the Python interpreter is set to use the one from the .venv folder. To do this:
Go to File -> Settings -> Project: <your_project_name> -> Python Interpreter.
Make sure that the interpreter is pointing to the Python executable inside the .venv folder (e.g., C:\Users\isumi\PycharmProjects\lca-baselines\.venv\Scripts\python.exe).
Verify the file path and Python version:

Ensure that the path to the Python executable in the error message is correct. If you're still facing issues, you can also try specifying the Python interpreter directly in your run configuration in PyCharm.
