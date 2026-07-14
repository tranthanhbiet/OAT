from oat.models.genome import Genome
from oat.parsers.parser_utils import FeatureBlock, normalize_blocks


def read_genbank(filename):
    """
    Read a GenBank file.

    Returns
    -------
    list[str]
        All lines in the GenBank file.
    """

    with open(filename, "r", encoding="utf-8") as infile:
        return infile.readlines()