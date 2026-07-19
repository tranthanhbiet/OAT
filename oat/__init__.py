"""
Organelle Annotation Toolkit (OAT)

Public API
"""

__version__ = "0.2.0"

from oat.io import read
from oat.consensus.merge import merge_genomes
from oat.validation import validate
from oat.export import write

__all__ = [
    "__version__",
    "read",
    "merge_genomes",
    "validate",
    "write",
]