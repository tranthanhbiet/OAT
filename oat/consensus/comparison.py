from __future__ import annotations

from oat.models.feature import Feature


class FeatureComparison:
    """
    Compare one biological feature across annotation sources.
    """

    def __init__(self, gene: str) -> None:
        """
        Parameters
        ----------
        gene : str
            Gene name being compared.
        """

        self.gene: str = gene

        self.features: dict[str, Feature | None] = {}

    def add(
        self,
        source: str,
        feature: Feature | None,
    ) -> None:
        """
        Add one Feature from one source.

        Parameters
        ----------
        source : str
            Annotation source.

        feature : Feature | None
            Feature object, or None if absent.
        """

        self.features[source] = feature

    def present(self, source: str) -> bool:
        """
        Return True if this source contains the feature.
        """

        return self.features.get(source) is not None

    @property
    def sources(self) -> int:
        """
        Number of annotation sources.
        """

        return len(self.features)

    @property
    def agreements(self) -> int:
        """
        Number of sources containing the feature.
        """

        return sum(
            feature is not None
            for feature in self.features.values()
        )

    @property
    def confidence(self) -> float:
        """
        Fraction of sources supporting this feature.
        """

        if self.sources == 0:
            return 0.0

        return self.agreements / self.sources

    def __repr__(self) -> str:

        return (
            f"FeatureComparison("
            f"gene='{self.gene}', "
            f"confidence={self.confidence:.2f})"
        )