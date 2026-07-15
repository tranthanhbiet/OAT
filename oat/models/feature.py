class Feature:
    """
    Represents one biological genome feature.
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

        # Sequence
        self.sequence = ""
        self.translation = ""

        # Annotation
        self.protein_id = ""
        self.anticodon = ""
        self.ec_number = ""
        self.note = ""

        # Extra qualifiers
        self.qualifiers = {}

        # Supporting evidence
        self.evidence = []

    def add_evidence(self, evidence):
        """
        Add one Evidence object.
        """
        self.evidence.append(evidence)

    @property
    def confidence(self):
        """
        Number of supporting evidence objects.
        """
        return len(self.evidence)

    def __repr__(self):
        return (
            f"Feature("
            f"type='{self.type}', "
            f"gene='{self.gene}', "
            f"confidence={self.confidence})"
        )
    @property
    def confidence_level(self):
        """
        Human-readable confidence level.
        """

        n = self.confidence

        if n >= 4:
            return "High"

        if n >= 2:
            return "Medium"

        return "Low"