class Evidence:
    """
    Represents one piece of annotation evidence.
    """

    def __init__(self):

        # Tool name
        self.source = ""

        # Version of the tool
        self.version = ""

        # Confidence (0.0–1.0)
        self.score = 1.0

        # Optional notes
        self.note = ""

    def __repr__(self):

        return (
            f"Evidence("
            f"source='{self.source}', "
            f"version='{self.version}', "
            f"score={self.score})"
        )