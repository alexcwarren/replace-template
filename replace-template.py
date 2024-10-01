import argparse
from pathlib import Path

import yaml


def load_replacements(config_file: str = "./replacements.yaml"):
    with open(config_file) as stream:
        try:
            print(yaml.safe_load(stream))
        except yaml.YAMLError as e:
            print(e)


def replace_keywords(path: Path, replacements: dict[str, str]):
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-path")

    args = parser.parse_args()
    print(args)

    load_replacements()
