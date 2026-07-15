from oat.parsers.base import BaseParser
from oat.parsers.parser_utils import (
    FeatureBlock,
    parse_location,
)


class GenBankParser(BaseParser):
    """
    Parser for GenBank (.gb/.gbk) files.
    """

    def read(self, filename):
        with open(filename, "r", encoding="utf-8") as infile:
            return infile.readlines()

    def parse_blocks(self, lines):
        """
        Parse GenBank FEATURES into FeatureBlock objects.
        """

        blocks = []

        in_features = False
        current = None

        valid_types = {
            "source",
            "gene",
            "CDS",
            "tRNA",
            "rRNA",
        }

        for line in lines:

            # Enter FEATURES section
            if line.startswith("FEATURES"):
                in_features = True
                continue

            # Stop before sequence
            if line.startswith("ORIGIN"):
                break

            if not in_features:
                continue

            # New feature
            if line.startswith("     "):

                feature_type = line[5:21].strip()

                if feature_type in valid_types:

                    location = line[21:].strip()

                    start, end, strand = parse_location(location)

                    current = FeatureBlock(
                        start=start,
                        end=end,
                        type=feature_type,
                    )

                    current.qualifiers["location"] = location
                    current.qualifiers["strand"] = strand

                    blocks.append(current)

                    continue

            # Qualifier
            if current is not None:

                stripped = line.strip()

                if stripped.startswith("/") and "=" in stripped:

                    key, value = stripped[1:].split("=", 1)

                    value = value.strip('"')

                    current.qualifiers[key] = value

        return blocks


def parse_genbank(filename):
    """
    Convenience function.
    """

    parser = GenBankParser()

    return parser.parse(filename)