# Copilot Instructions for My Python Project

This document provides context and conventions for GitHub Copilot when working in this repository.

## CI/CD

### GitHub Actions Workflows
- **ci.yml** - Runs on push/PR to main/develop branches
  - Tests against Python 3.9, 3.10, 3.11, 3.12
  - Runs linting (flake8), formatting (Black), type checking (mypy)
  - Generates coverage reports
  - Uploads coverage to Codecov
- **release.yml** - Triggers on version tags (e.g., v1.0.0)
  - Builds distributable packages
  - Creates GitHub releases

### Checking CI Status
```bash
# View workflow runs
gh run list

# View specific run details
gh run view <run-id>
```

## Build, Test, and Lint Commands

### Setup
```bash
# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt
```

### Testing
```bash
# Run all tests
pytest

# Run a specific test file
pytest tests/test_main.py

# Run a specific test function
pytest tests/test_main.py::test_greet

# Run with coverage
pytest --cov=src --cov-report=html
```

### Linting and Formatting
```bash
# Format code with Black (line length: 88)
black src/ tests/

# Check formatting without making changes
black --check src/ tests/

# Lint with flake8
flake8 src/ tests/ --max-line-length=88

# Type checking with mypy
mypy src/ --ignore-missing-imports

# Security scanning
bandit -r src/
safety check
```

## Architecture

This is a Python project following a clean architecture pattern:

- **src/** - Main application code
  - `main.py` - Entry point and basic functions
  - `user.py` - User domain model and repository pattern
  - `utils.py` - Shared utility functions
  - `config.py` - Configuration management from environment
- **tests/** - Test files using pytest
  - `conftest.py` - Shared fixtures
  - Test files mirror src/ structure (`test_*.py`)
- **requirements.txt** - Project dependencies

### Design Patterns Used
- **Repository Pattern**: See `UserRepository` in `user.py` for data access abstraction
- **Dataclasses**: Used for domain models (e.g., `User`, `Config`)
- **Environment-based Configuration**: Config loaded from env vars with defaults

## Key Conventions

### Code Style
- Use **Black** for code formatting (line length: 88 characters)
- Follow **PEP 8** style guidelines
- Use **type hints** for function signatures

### Testing
- All test files should be in the `tests/` directory
- Test file names must start with `test_` and mirror the source module name
- Test function names must start with `test_`
- Use **pytest** fixtures for setup/teardown (see `conftest.py` for shared fixtures)
- Group related tests in classes (e.g., `TestUserRepository`)
- Use `@pytest.mark.parametrize` for testing multiple inputs (see `test_utils.py`)
- Use `monkeypatch` fixture for environment variable testing (see `test_config.py`)

### Imports
- Standard library imports first
- Third-party imports second
- Local imports last
- Each group separated by a blank line

### Documentation
- Use **docstrings** for all public functions, classes, and modules
- Follow Google-style docstring format (see examples in `user.py`)
- Include type information in docstrings when helpful
- Document:
  - **Args**: Parameter descriptions with types
  - **Returns**: What the function returns
  - **Raises**: Any exceptions that may be raised

### Error Handling
- Raise `ValueError` for invalid input data (see `UserRepository.create`)
- Use Optional[T] return types when a function may return None
- Prefer explicit exception handling over silent failures

## Virtual Environment
Always ensure the virtual environment is activated before running commands. The project uses `venv` for isolation.

## Pre-commit Checks
Before committing code, ensure:
1. All tests pass: `pytest`
2. Code is formatted: `black src/ tests/`
3. No linting errors: `flake8 src/ tests/`
4. Type hints are correct: `mypy src/`

The CI workflow will verify these automatically on push.
