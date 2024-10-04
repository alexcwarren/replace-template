# replace-template

Script to automate keyword replacement in provided repo created from a template

## How to install dependencies

```shell
python -m pip install .
```

### Use *editable mode* for development

```shell
python -m pip install -e .
```

> This enables `pytest` to acknowledge local code changes instead of only looking
> at "frozen" versions of installed packages.

## How to run tests with `pytest`

```shell
pytest tests
```

### How to run `pytest` to allow terminal output (e.g. print statements)

```shell
pytest -s tests
```

## How to setup pre-commit Git Hook

```shell
python -m pre-commit install
```
