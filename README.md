# Automating Python Projects with Pip, PyPI & Scripting

A small automation toolkit built to practice pip, PyPI packages, virtual environments, and command-line scripting in Python.

## What's Included

| File | Purpose |
|------|---------|
| `lib/generate_log.py` | `generate_log(data)` validates a list, writes it to a dated file (`log_YYYYMMDD.txt`), prints a confirmation, and returns the filename. |
| `automation_tool.py` | Uses the `requests` package to fetch a post from a public API and saves it to `post_output.csv`. |
| `task_cli.py` | An `argparse` CLI with OOP classes (`Task`, `User`, `TaskStore`) to add and complete tasks. |
| `testing/test_generate_log.py` | Pytest tests for `generate_log`. |
| `requirements.txt` | Pinned dependencies for reproducible installs. |

## Setup

Use a virtual environment so packages stay isolated from your system Python:

```bash
python3 -m venv venv
source venv/bin/activate      
pip install -r requirements.txt
```

To record new dependencies after installing a package:

```bash
pip freeze > requirements.txt
```

## Usage

**Generate a log file**

```bash
python3 -c "from lib.generate_log import generate_log; generate_log(['User logged in', 'Report exported'])"
```

**Fetch data from an API and save it to CSV**

```bash
python3 automation_tool.py
```

**Manage tasks from the command line**

```bash
python3 task_cli.py add-task --user alice "Buy milk"
python3 task_cli.py complete-task --user alice "Buy milk"
python3 task_cli.py list-tasks --user alice
```

Tasks are saved to `tasks.json`.

## Running Tests

```bash
python3 -m pytest
```

## Project Structure

```
.
├── lib/
│   ├── __init__.py
│   └── generate_log.py
├── testing/
│   ├── __init__.py
│   └── test_generate_log.py
├── automation_tool.py
├── task_cli.py
├── requirements.txt
├── Pipfile
├── pytest.ini
└── README.md
```

## Concepts Practiced

- Installing and tracking packages with `pip` and `requirements.txt`
- Isolating dependencies with virtual environments
- Separating concerns with small, commented functions
- Wrapping script logic in `if __name__ == "__main__":`
- File I/O with `.txt` and `.csv` output
- Command-line interfaces with `argparse` and object-oriented design
- Git workflow: feature branch, commit, push, pull request, merge