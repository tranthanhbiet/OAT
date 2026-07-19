class GeneComparison:
    """
    Comparison for one gene across genomes.
    """

    def __init__(self, gene):

        self.gene = gene

        self.sources = {}

    def add(self, source, present):

        self.sources[source] = present

    @property
    def agreement(self):

        return len(set(self.sources.values())) == 1

    def __repr__(self):

        return (
            f"GeneComparison("
            f"{self.gene}, "
            f"{self.sources})"
        )