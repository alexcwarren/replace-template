# replace-template

Script to automate keyword replacement in provided repo created from a template.

Intended to be used alongside **[python-project template repo](https://www.github.com/alexcwarren/python-project)**.

## Usage

Create a new repo using the aforementioned **[python-project template repo](https://www.github.com/alexcwarren/python-project)**.

Clone your new repo to your computer.

Clone **this** repo to your computer:

  ```shell
  git clone https://www.github.com/alexcwarren/replace-template.git
  ```

On your computer, navigate to the **replace_template** directory (where you cloned it).

Install **replace_template**:

  ```shell
  python -m pip install .
  ```

Modify the `replacement.yaml` file to use the **keywords** and **replacements** you like.

Run `replacement_template.py` on your new repo directory (let's say it's called `new_repo`):

```shell
python replacement_template.py ../new_repo/
```

You should now have all **keywords** replaced with their respective **replacements**.

### Install in *editable mode* for development

```shell
python -m pip install -e .
```

> This enables `pytest` to acknowledge local code changes instead of only looking
> at "frozen" versions of installed packages.

### How to run tests with `pytest`

```shell
pytest tests
```

#### How to run `pytest` to allow terminal output (e.g. print statements)

```shell
pytest -s tests
```

### How to setup pre-commit Git Hook

```shell
python -m pre-commit install
```
