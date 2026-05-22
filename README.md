# My Python Project

[![CI](https://github.com/ericfigueroa82/my-python-project/actions/workflows/ci.yml/badge.svg)](https://github.com/ericfigueroa82/my-python-project/actions/workflows/ci.yml)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Python project demonstrating best practices including CI/CD, testing, type hints, and comprehensive documentation.

## Setup

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Running the Application

```bash
# Run the main application
python -m src.main

# Or run directly
python src/main.py
```

## Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov-report=html

# Run a specific test file
pytest tests/test_user.py

# Run a specific test function
pytest tests/test_user.py::TestUserRepository::test_create_user
```

## Code Quality

```bash
# Format code
black src/ tests/

# Lint code
flake8 src/ tests/

# Type checking
mypy src/

# Security scanning
bandit -r src/
```

## Project Structure

```
my-python-project/
├── .github/
│   ├── workflows/           # GitHub Actions CI/CD
│   └── copilot-instructions.md
├── src/                     # Source code
│   ├── main.py             # Entry point
│   ├── user.py             # User model & repository
│   ├── utils.py            # Utility functions
│   └── config.py           # Configuration management
├── tests/                   # Test files
│   ├── conftest.py         # Shared fixtures
│   ├── test_main.py
│   ├── test_user.py
│   ├── test_utils.py
│   └── test_config.py
├── requirements.txt         # Project dependencies
├── .gitignore
└── README.md
```

## Features

- ✅ **Type Hints**: Full type annotations for better code quality
- ✅ **Testing**: Comprehensive test suite with pytest
- ✅ **CI/CD**: Automated testing and linting via GitHub Actions
- ✅ **Code Quality**: Black formatting, flake8 linting, mypy type checking
- ✅ **Security**: Bandit security scanning
- ✅ **Documentation**: Google-style docstrings and comprehensive README

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License.
