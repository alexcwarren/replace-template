import argparse
from pathlib import Path

import yaml


def load_replacements(config_file: str):
    """TODO"""
    replacements: dict = None
    with open(config_file) as stream:
        try:
            replacements = yaml.safe_load(stream)
        except yaml.YAMLError as e:
            print(f"ERROR: Could not parse {config_file}.")
            print(e)
    return replacements


def replace_keywords(project_dir: str, replacements: dict[str, str]):
    """TODO"""
    project_path: Path = Path(project_dir)
    for item in project_path.iterdir():
        # Ignore hidden files/folders (starting with ".")
        if not item.name.startswith("."):
            # print(item.name, end=": ")
            # Replace any keywords in item name
            for keyword, replacement in replacements.items():
                if keyword in item.name:
                    # print(item.name.replace(keyword, replacement))
                    pass
            # print()
            # If item is dir, call replace_keywords on item
            # If item is file, replace any keywords in its contents


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("project_path")
    parser.add_argument("--config-file", "-c")

    args = parser.parse_args()

    # Assign to command-line arg or use default if none provided
    config_file: str = args.config_file or "./replacements.yaml"
    replacements: dict = load_replacements(config_file)
    replace_keywords(args.project_path, replacements)
