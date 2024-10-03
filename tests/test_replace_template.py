from pathlib import Path

import pytest
import yaml
from directory import Directory

import replace_template as rt


@pytest.fixture
def test_dir(request: pytest.FixtureRequest, project_path: str) -> Directory:
    """TODO"""
    # Get command-line arg value of variable(s) defined in conftest.py
    keep_test_dir: bool = request.config.getoption("--keep-test-dir")
    seed = request.config.getoption("--seed")

    # Create test directory and its contents
    testdir: Directory = Directory(Path.cwd(), get_keywords(project_path), seed=seed)

    # Create nested function to call upon pytest conclusion
    def finalizer():
        if not keep_test_dir:
            # Remove test directory and all its contents
            testdir.remove_all()

    # Add nested function as "finalizer" (function to call upon pytest conclusion)
    request.addfinalizer(finalizer)

    return testdir


def get_keywords(project_path: str) -> list[str]:
    """TODO"""
    config_file: str = f"{project_path}/replacements.yaml"

    replacements_dict: dict = None
    with open(config_file) as stream:
        try:
            replacements_dict = yaml.safe_load(stream)
        except yaml.YAMLError as e:
            print(e)
    assert replacements_dict is not None
    return list(replacements_dict.keys())


def test_load_replacements(config_path: str):
    """TODO"""
    assert rt.load_replacements(config_path) is not None


def test_replace_template(test_dir: Directory, config_path: str):
    """TODO"""
    replacements: dict[str, str] = rt.load_replacements(config_path)
    rt.replace_keywords(test_dir.path, replacements)
