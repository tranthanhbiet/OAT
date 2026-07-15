"""
Open Annotation Toolkit (OAT)

Public API
"""

from oat.io import read
from oat.consensus.merge import merge_genomes
from oat.validation.pipeline import validate

__all__ = [
    "read",
    "merge_genomes",
    "validate",
]