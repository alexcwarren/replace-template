import pytest


def pytest_addoption(parser: pytest.Parser):
    """TODO"""
    parser.addoption("--keep-test-dir", action="store_true")
    parser.addoption("--seed")
    parser.addoption("--replacements-file", default="replacements.yaml")


@pytest.fixture
def project_path(request: pytest.FixtureRequest) -> str:
    """TODO"""
    return str(request.config.rootpath)


@pytest.fixture
def config_path(request: pytest.FixtureRequest, project_path: str) -> str:
    """TODO"""
    return f"{project_path}\\{request.config.getoption('--replacements-file')}"
