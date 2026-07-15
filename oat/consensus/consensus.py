class ConsensusGenome:
    """
    Represents a merged annotation from multiple sources.
    """

    def __init__(self):

        self.features = []

        self.sources = []

    def add_source(self, source):

        if source not in self.sources:
            self.sources.append(source)

    def __repr__(self):

        return (
            f"ConsensusGenome("
            f"sources={len(self.sources)}, "
            f"features={len(self.features)})"
        )