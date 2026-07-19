"""
Canonical gene naming utilities.
"""

from oat.naming.aliases import ALIASES


def canonical_gene(name):
    """
    Return the canonical gene name.

    Unknown names are returned unchanged.
    """

    if not name:
        return ""

    key = name.strip().lower()

    return ALIASES.get(key, name)