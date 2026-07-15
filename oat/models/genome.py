class Genome:
    """
    Represents an annotated genome.
    """

    def __init__(self):

        # Basic information
        self.name = ""
        self.organism = ""
        self.definition = ""
        self.accession = ""

        # Sequence information
        self.sequence = ""
        self.length = 0

        # Genome properties
        self.topology = "circular"
        self.molecule_type = "DNA"
        self.genetic_code = 1

        # Annotation
        self.features = []

    def validate(self, expected_genes=None):
        """
        Validate this genome.
        """
        from oat.validation.pipeline import validate

        return validate(
            self,
            expected_genes=expected_genes,
        )

    def merge(self, *others):
        """
        Merge this genome with one or more genomes.
        """
        from oat.consensus.merge import merge_genomes

        return merge_genomes(
            [self] + list(others)
        )