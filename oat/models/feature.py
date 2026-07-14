class Feature:
    """
    Represents a genomic feature (CDS, tRNA, rRNA, ORF, etc.).
    """

    def __init__(self):
        self.type = ""
        self.gene = ""
        self.product = ""
        self.start = 0
        self.end = 0
        self.strand = "+"
        self.sequence = ""
        self.translation = ""
        self.qualifiers = {}
        self.evidence = []