class FeatureConflict:
    """
    Represents one disagreement among annotation sources.
    """

    def __init__(self, gene, kind, message):

        self.gene = gene
        self.kind = kind
        self.message = message

    def __repr__(self):

        return (
            f"FeatureConflict("
            f"gene='{self.gene}', "
            f"kind='{self.kind}')"
        )