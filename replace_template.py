import argparse
from pathlib import Path

import yaml

INVALID_CHARACTERS: str = '<>:"/\\|?*'


def load_replacements(config_file: str):
    """TODO"""
    replacements: dict = dict()
    with open(config_file) as stream:
        try:
            replacements = yaml.safe_load(stream)
        except yaml.YAMLError as e:
            print(f"ERROR: Could not parse {config_file}.")
            print(e)
    return replacements


def replace_keywords(project_dir: str, replacements: dict[str, str]) -> None:
    """TODO"""
    project_path: Path = Path(project_dir)
    for item in project_path.iterdir():
        # Replace any keywords in item name
        for keyword, replacement in replacements.items():
            # Rename the file/directory
            if keyword in item.name:
                # Check for invalid file/directory name characters
                for ch in INVALID_CHARACTERS:
                    if ch in replacement:
                        print(
                            f"WARNING: Cannot rename {item.name} with {replacement}."
                            + f' Invalid character "{ch}".'
                        )
                item = item.rename(
                    item.with_name(item.name.replace(keyword, replacement))
                )

        if item.is_dir():
            replace_keywords(str(item), replacements)
        else:
            file_contents: str = ""
            with item.open("r") as file:
                file_contents = file.read()

            with item.open("w") as file:
                file.write(file_contents.replace(keyword, replacement))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("project_path")
    parser.add_argument("--config-file", "-c")

    args = parser.parse_args()

    # Assign to command-line arg or use default if none provided
    config_file: str = args.config_file or "./replacements.yaml"
    replacements: dict = load_replacements(config_file)
    replace_keywords(args.project_path, replacements)
