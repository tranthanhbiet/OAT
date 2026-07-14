from oat.models.genome import Genome
from oat.parsers.parser_utils import FeatureBlock, normalize_blocks


def read_tbl(filename):
    """
    Read an NCBI Feature Table (.tbl).
    """
    with open(filename, "r", encoding="utf-8") as infile:
        return infile.readlines()


def parse_blocks(lines):
    """
    Parse an NCBI Feature Table into FeatureBlock objects.
    """

    blocks = []
    current = None

    for line in lines:

        fields = line.rstrip().split("\t")

        # -----------------------------------------
        # New feature block
        # -----------------------------------------
        if len(fields) >= 3 and fields[2] != "":

            current = FeatureBlock(
                start=int(fields[0]),
                end=int(fields[1]),
                type=fields[2]
            )

            blocks.append(current)
            continue

        # -----------------------------------------
        # Qualifier
        # -----------------------------------------
        if current is not None and len(fields) >= 5:

            key = fields[3]
            value = fields[4]

            current.qualifiers[key] = value

    return blocks


def parse_tbl(filename):
    """
    Parse an NCBI Feature Table (.tbl)
    into an OAT Genome object.
    """

    genome = Genome()

    lines = read_tbl(filename)

    blocks = parse_blocks(lines)

    genome.features = normalize_blocks(blocks)

    return genome