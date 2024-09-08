import os
import yaml

def create_project_structure(project_name, config_file):
  with open(config_file, 'r') as f:
    config = yaml.safe_load(f)

  root_dir = os.path.join(os.getcwd(), project_name)
  os.makedirs(root_dir, exist_ok=True)

  for subdir, config_data in config.items():
    subdir_path = os.path.join(root_dir, subdir)
    os.makedirs(subdir_path, exist_ok=True)

    if 'files' in config_data:
      for file_name, file_content in config_data['files'].items():
        file_path = os.path.join(subdir_path, file_name)
        with open(file_path, 'w') as f:
          f.write(file_content)
