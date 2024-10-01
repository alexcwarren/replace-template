import random
import shutil
from pathlib import Path

import pytest

import replace_template as rt


class Directory:
    def __init__(
        self,
        parent_dir: str,
        max_num_folders: int = 10,
        max_num_files: int = 10,
        seed: int = 1234,
    ):
        parent_path: Path = Path(parent_dir)

        test_dir: str = "test_dir"
        self.__test_path: Path = parent_path.joinpath(test_dir)

        if self.__test_path.exists():
            self.remove_all()

        self.__test_path.mkdir(parents=True)

        self.__create_contents()

    def __create_contents(self):
        """TODO"""
        pass
        # Create 1 to max number of folders.

        # In each folder, create 1 to max number of files.

        # In each file, populate with random text intersparsed with at least 1 of each
        # keyword.

    def remove_all(self):
        shutil.rmtree(self.__test_path)


@pytest.fixture
def test_dir(request) -> Directory:
    """TODO"""
    # Get command-line arg value of variable(s) defined in conftest.py
    keep_test_dir: bool = request.config.getoption("--keep-test-dir")

    # Create test directory and its contents
    testdir: Directory = Directory(Path.cwd())

    # Create nested function to call upon pytest conclusion
    def finalizer():
        if not keep_test_dir:
            # Remove test directory and all its contents
            testdir.remove_all()

    # Add nested function as "finalizer" (function to call upon pytest conclusion)
    request.addfinalizer(finalizer)

    return testdir


def test_load_replacements():
    """TODO"""
    dir_level: str = ".." if Path.cwd().name == "tests" else "."
    replacements: dict = rt.load_replacements(f"{dir_level}/replacements.yaml")
    print(replacements)


def test_replace_template(test_dir):
    """TODO"""
    print(test_dir)
