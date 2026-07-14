from oat.parsers.base import BaseParser
from oat.parsers.parser_utils import FeatureBlock


class TBLParser(BaseParser):
    """
    Parser for NCBI Feature Table (.tbl) files.
    """

    def read(self, filename):
        with open(filename, "r", encoding="utf-8") as infile:
            return infile.readlines()

    def parse_blocks(self, lines):

        blocks = []
        current = None

        for line in lines:

            fields = line.rstrip().split("\t")

            # New feature block
            if len(fields) >= 3 and fields[2] != "":

                current = FeatureBlock(
                    start=int(fields[0]),
                    end=int(fields[1]),
                    type=fields[2],
                )

                blocks.append(current)
                continue

            # Qualifier
            if current is not None and len(fields) >= 5:

                key = fields[3]
                value = fields[4]

                current.qualifiers[key] = value

        return blocks


def parse_tbl(filename):
    """
    Convenience function.
    """

    parser = TBLParser()

    return parser.parse(filename)