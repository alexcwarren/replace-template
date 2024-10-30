from directory import Directory

import replace_template as rt


def test_load_replacements(config_path: str):
    """TODO"""
    assert rt.load_replacements(config_path) is not None


def test_replace_template(test_dir: Directory, config_path: str):
    """TODO"""
    replacements: dict[str, str] = rt.load_replacements(config_path)
    rt.replace_keywords(test_dir.path, replacements)

    testdir_contents: dict = test_dir.traverse()

    for keyword in replacements:
        # Ensure no keywords left "un-replaced"
        assert not any(keyword in item for item in testdir_contents)
