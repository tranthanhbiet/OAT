from __future__ import annotations

from oat.consensus.comparison import FeatureComparison
from oat.conflicts.conflict import FeatureConflict


class GenomeComparison:
    """
    Collection of FeatureComparison objects.
    """

    def __init__(self) -> None:

        self.comparisons: dict[str, FeatureComparison] = {}

    def add(
        self,
        comparison: FeatureComparison,
    ) -> None:
        """
        Add a FeatureComparison.
        """

        self.comparisons[comparison.gene] = comparison

    def get(
        self,
        gene: str,
    ) -> FeatureComparison | None:
        """
        Return one comparison.
        """

        return self.comparisons.get(gene)

    def __iter__(self):

        return iter(self.comparisons.values())

    def __len__(self) -> int:

        return len(self.comparisons)

    def summary(self) -> str:
        """
        Return a simple text summary.
        """

        lines: list[str] = []

        lines.append("Genome Comparison")
        lines.append("=" * 40)
        lines.append("")

        for comparison in sorted(
            self.comparisons.values(),
            key=lambda c: c.gene.lower(),
        ):

            level = (
                "High"
                if comparison.confidence == 1
                else "Partial"
            )

            lines.append(
                f"{comparison.gene:<12}"
                f"{comparison.confidence:.2f}   "
                f"{level}"
            )

        return "\n".join(lines)

    def find_conflicts(self) -> list[FeatureConflict]:
        """
        Detect annotation conflicts.
        """

        conflicts: list[FeatureConflict] = []

        for comparison in self:

            if comparison.agreements != comparison.sources:

                conflicts.append(
                    FeatureConflict(
                        gene=comparison.gene,
                        kind="presence",
                        message=(
                            f"Present in "
                            f"{comparison.agreements}/"
                            f"{comparison.sources} sources"
                        ),
                    )
                )

        return conflicts

    def __repr__(self) -> str:

        return (
            f"GenomeComparison("
            f"{len(self)} features)"
        )
