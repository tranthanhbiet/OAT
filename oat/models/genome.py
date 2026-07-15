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