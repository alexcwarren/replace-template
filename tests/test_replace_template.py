import shutil
from pathlib import Path

import pytest

# import replace_template as rt


class TestDirectory:
    def __init__(self, parent_dir: str):
        parent_path: Path = Path(parent_dir)
        test_dir: str = "test_dir"
        self.__test_path: Path = parent_path.joinpath(test_dir)
        if self.__test_path.exists():
            self.remove_all()
        self.__test_path.mkdir(parents=True)

    def remove_all(self):
        shutil.rmtree(self.__test_path)


@pytest.fixture
def test_dir(request) -> TestDirectory:
    """TODO"""
    # Get command-line arg value of variable(s) defined in conftest.py
    keep_test_dir: bool = request.config.getoption("--keep-test-dir")

    # Create test directory and its contents
    testdir: TestDirectory = TestDirectory(Path.cwd())

    # Create nested function to call upon pytest conclusion
    def finalizer():
        if not keep_test_dir:
            # Remove test directory and all its contents
            testdir.remove_all()

    # Add nested function as "finalizer" (function to call upon pytest conclusion)
    request.addfinalizer(finalizer)

    return testdir


def test_replace_template(test_dir):
    """TODO"""
    print(test_dir)
