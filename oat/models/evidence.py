from __future__ import annotations


class Evidence:
    """
    Represents one piece of annotation evidence.
    """

    def __init__(self) -> None:

        # Tool name
        self.source: str = ""

        # Version of the tool
        self.version: str = ""

        # Confidence score (0.0–1.0)
        self.score: float = 1.0

        # Optional notes
        self.note: str = ""

    def __repr__(self) -> str:

        return (
            f"Evidence("
            f"source='{self.source}', "
            f"version='{self.version}', "
            f"score={self.score})"
        )