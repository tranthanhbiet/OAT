from oat.models.genome import Genome
from oat.parsers.parser_utils import normalize_blocks


class BaseParser:
    """
    Base class for all annotation parsers.
    """

    def read(self, filename):
        """
        Read an annotation file.

        Must return a list of lines.
        """
        raise NotImplementedError

    def parse_blocks(self, lines):
        """
        Convert file lines into FeatureBlock objects.
        """
        raise NotImplementedError

    def parse(self, filename):
        """
        Parse an annotation file into an OAT Genome.
        """

        lines = self.read(filename)

        blocks = self.parse_blocks(lines)

        genome = Genome()

        genome.features = normalize_blocks(blocks)

        return genome