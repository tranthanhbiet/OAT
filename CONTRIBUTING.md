# Contributing to OAT

Thank you for your interest in contributing to OAT!

We welcome bug reports, feature requests, documentation improvements, and code contributions.

---

# Development Setup

Clone the repository:

```bash
git clone https://github.com/<your_username>/OAT.git
cd OAT
```

Install OAT in editable mode:

```bash
python -m pip install -e .
```

Install development dependencies if needed.

---

# Running Tests

Run all tests before submitting a contribution.

```bash
pytest
```

All tests should pass before opening a Pull Request.

---

# Coding Style

Please follow the existing coding style:

- Use descriptive variable names.
- Add docstrings to public functions and classes.
- Keep functions focused on a single responsibility.
- Prefer readability over clever code.

---

# Pull Requests

Before submitting a Pull Request:

- Run the complete test suite.
- Update documentation if necessary.
- Add tests for new functionality.
- Update the CHANGELOG when appropriate.

---

# Reporting Issues

When reporting a bug, please include:

- OAT version
- Python version
- Operating system
- Input file (if possible)
- Complete error message