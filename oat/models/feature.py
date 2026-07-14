class Feature:
    """
    Represents a genomic feature.
    """

    def __init__(self):

        # Identity
        self.type = ""
        self.gene = ""
        self.product = ""

        # Coordinates
        self.start = 0
        self.end = 0
        self.strand = "+"

        # Sequences
        self.sequence = ""
        self.translation = ""

        # Annotation
        self.protein_id = ""
        self.anticodon = ""
        self.ec_number = ""
        self.note = ""

        # Additional qualifiers
        self.qualifiers = {}

        # Supporting evidence
        self.evidence = []