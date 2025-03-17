import os
import yaml

# Function to check if the directory exists
def check_path_exists(path):
    if os.path.exists(path):
        return True
    else:
        return False

# Read the YAML file
yaml_file = r"C:\Users\isumi\PycharmProjects\lca-baselines\ci-builds-repair\ci-builds-repair-benchmark\config.yaml"

# Load the YAML content
with open(yaml_file, 'r') as file:
    config = yaml.safe_load(file)

# List of paths to check
paths = [
    config.get('repos_folder'),
    config.get('out_folder'),
    config.get('data_cache_dir'),
    config.get('file_change_info_dir'),
    config.get('extracted_errors_folder')
]

# Check each path and print the result
for path in paths:
    if path:
        if check_path_exists(path):
            print(f"Path exists: {path}")
        else:
            print(f"Path does not exist: {path}")
    else:
        print("Path is empty or missing.")
