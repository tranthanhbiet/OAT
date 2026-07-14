class Evidence:
    """
    Represents evidence supporting a genomic feature.
    """

    def __init__(self):
        self.source = ""
        self.identity = 0.0
        self.coverage = 0.0
        self.score = 0.0
        self.note = ""