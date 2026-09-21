# caps_5001_fall_2026

## Setup

```bash
python3.11 -m venv .my_venv
source .my_venv/bin/activate
python -m pip install -r requirements.txt
```

## Run Pylint

Activate the virtual environment each time you open a new terminal:

```bash
source .my_venv/bin/activate
```

This folder currently contains notebooks rather than standalone Python files, so the commands below are most useful once you add `.py` files to the repository.

The repository includes a `.pylintrc` file. Run pylint from the repository root and pass `--rcfile=.pylintrc` explicitly so those settings are always used.

Run pylint on one Python file:

```bash
python -m pylint --rcfile=.pylintrc path/to/file.py
```

Run pylint on all Python files in the repository, excluding the virtual environment:

```bash
find . -path './.my_venv' -prune -o -type f -name "*.py" -exec python -m pylint --rcfile=.pylintrc {} +
```

Run with a short report at the end:

```bash
python -m pylint --rcfile=.pylintrc --reports=y path/to/file.py
```

If you add new packages later, install them into the active virtual environment:

```bash
python -m pip install <package-name>
```