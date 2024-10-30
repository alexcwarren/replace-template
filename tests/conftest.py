import random
import sys
from pathlib import Path

import pytest
import yaml
from directory import Directory


def pytest_addoption(parser: pytest.Parser):
    """TODO"""
    parser.addoption("--keep-test-dir", action="store_true")
    parser.addoption("--seed")
    parser.addoption("--replacements-file", default="replacements.yaml")


@pytest.fixture(scope="session")
def project_path(request: pytest.FixtureRequest) -> str:
    """TODO"""
    return str(request.config.rootpath)


@pytest.fixture(scope="session")
def config_path(request: pytest.FixtureRequest, project_path: str) -> str:
    """TODO"""
    return f"{project_path}\\{request.config.getoption('--replacements-file')}"


@pytest.fixture(scope="session")
def test_dir(request: pytest.FixtureRequest, project_path: str) -> Directory:
    """TODO"""
    # Get command-line arg value of variable(s) defined in conftest.py
    keep_test_dir: bool = request.config.getoption("--keep-test-dir")
    seed = request.config.getoption("--seed") or str(random.randrange(sys.maxsize))

    # Create test directory and its contents
    testdir: Directory = Directory(
        str(Path.cwd()), get_keywords(project_path), seed=seed
    )

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

    replacements_dict: dict = dict()
    with open(config_file) as stream:
        try:
            replacements_dict = yaml.safe_load(stream)
        except yaml.YAMLError as e:
            print(e)
    assert replacements_dict is not None
    return list(replacements_dict.keys())
