"""
Validation framework for OAT.
"""

from oat.validation.pipeline import validate
from oat.validation.report import ValidationReport

__all__ = [
    "validate",
    "ValidationReport",
]