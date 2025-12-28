# Contributing to Learning Path Analyzer

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## How to Contribute

### Reporting Bugs

1. Check if the bug has already been reported in Issues
2. If not, create a new issue with:
   - Clear title and description
   - Steps to reproduce
   - Expected vs actual behavior
   - Your environment (OS, Python version)

### Suggesting Enhancements

1. Check if the enhancement has been suggested
2. Create an issue describing:
   - The problem you're trying to solve
   - Your proposed solution
   - Why this enhancement would be useful

### Pull Requests

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes
4. Write or update tests
5. Ensure all tests pass: `pytest tests/`
6. Ensure code follows style guide: `black src/ tests/` and `flake8 src/ tests/`
7. Commit with clear message: `git commit -m "Add feature: description"`
8. Push to your fork: `git push origin feature/your-feature-name`
9. Open a Pull Request

## Development Setup

```bash
# Clone your fork
git clone https://github.com/your-username/Learning_Path_Analyzer.git
cd Learning_Path_Analyzer

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies including dev tools
pip install -r requirements.txt

# Run tests
pytest tests/
```

## Code Style

- Follow PEP 8
- Use Black for formatting: `black src/ tests/`
- Use flake8 for linting: `flake8 src/ tests/`
- Write docstrings for functions and classes
- Add type hints where appropriate

## Testing

- Write unit tests for new features
- Ensure test coverage doesn't decrease
- Run `pytest tests/ --cov=src` to check coverage

## Questions?

Feel free to open an issue for any questions!
