from __future__ import annotations

from typing import Any

from oat.models.evidence import Evidence


class Feature:
    """
    Represents one biological genome feature.
    """

    def __init__(self) -> None:

        # Identity
        self.type: str = ""
        self.gene: str = ""
        self.product: str = ""

        # Coordinates
        self.start: int = 0
        self.end: int = 0
        self.strand: str = "+"

        # Sequence
        self.sequence: str = ""
        self.translation: str = ""

        # Annotation
        self.protein_id: str = ""
        self.anticodon: str = ""
        self.ec_number: str = ""
        self.note: str = ""

        # Extra qualifiers
        self.qualifiers: dict[str, Any] = {}

        # Supporting evidence
        self.evidence: list[Evidence] = []

    def add_evidence(self, evidence: Evidence) -> None:
        """
        Add one Evidence object.
        """
        self.evidence.append(evidence)

    @property
    def confidence(self) -> int:
        """
        Number of supporting evidence objects.
        """
        return len(self.evidence)

    @property
    def confidence_level(self) -> str:
        """
        Human-readable confidence level.
        """

        n = self.confidence

        if n >= 4:
            return "High"

        if n >= 2:
            return "Medium"

        return "Low"

    def __repr__(self) -> str:
        return (
            f"Feature("
            f"type='{self.type}', "
            f"gene='{self.gene}', "
            f"confidence={self.confidence})"
        )