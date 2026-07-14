class Genome:
    """
    Represents a complete organelle genome.
    """

    def __init__(self):
        self.name = ""
        self.organism = ""
        self.sequence = ""
        self.topology = "circular"
        self.genetic_code = 1
        self.features = []
        self.metadata = {}