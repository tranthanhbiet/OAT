from __future__ import annotations

from oat.models.feature import Feature


class Genome:
    """
    Represents an annotated genome.
    """

    def __init__(self) -> None:

        # Basic information
        self.name: str = ""
        self.organism: str = ""
        self.definition: str = ""
        self.accession: str = ""

        # Sequence information
        self.sequence: str = ""
        self.length: int = 0

        # Genome properties
        self.topology: str = "circular"
        self.molecule_type: str = "DNA"
        self.genetic_code: int = 1

        # Annotation source
        self.source: str = ""

        # Annotation
        self.features: list[Feature] = []

    def validate(self, expected_genes: list[str] | None = None):
        """
        Validate this genome.
        """
        from oat.validation.pipeline import validate

        return validate(
            self,
            expected_genes=expected_genes,
        )

    def merge(self, *others: "Genome"):
        """
        Merge this genome with one or more genomes.
        """
        from oat.consensus.merge import merge_genomes

        return merge_genomes(
            [self] + list(others)
        )

    def summary(self) -> str:
        """
        Return a summary of the genome.
        """

        n_cds = sum(
            f.type == "CDS"
            for f in self.features
        )

        n_trna = sum(
            f.type == "tRNA"
            for f in self.features
        )

        n_rrna = sum(
            f.type == "rRNA"
            for f in self.features
        )

        lines = [
            f"Organism : {self.organism}",
            f"Accession: {self.accession}",
            f"Length   : {self.length} bp",
            f"Topology : {self.topology}",
            "",
            f"CDS  : {n_cds}",
            f"tRNA : {n_trna}",
            f"rRNA : {n_rrna}",
            f"Total: {len(self.features)}",
        ]

        return "\n".join(lines)

    def find(self, gene: str) -> Feature | None:
        """
        Find a feature by gene name.

        Returns
        -------
        Feature | None
        """

        for feature in self.features:

            if feature.gene == gene:
                return feature

        return None

    def filter(self, **kwargs) -> list[Feature]:
        """
        Filter features by attribute.

        Examples
        --------
        genome.filter(type="tRNA")

        genome.filter(type="CDS", strand="-")
        """

        results: list[Feature] = []

        for feature in self.features:

            keep = True

            for key, value in kwargs.items():

                if not hasattr(feature, key):

                    keep = False
                    break

                if getattr(feature, key) != value:

                    keep = False
                    break

            if keep:

                results.append(feature)

        return results

    def count(self, **kwargs) -> int:
        """
        Count features.

        Examples
        --------
        genome.count()

        genome.count(type="CDS")

        genome.count(type="tRNA", strand="-")
        """

        if not kwargs:
            return len(self.features)

        return len(self.filter(**kwargs))

    def statistics(self) -> dict[str, int]:
        """
        Return genome statistics.
        """

        stats = {
            "features": len(self.features),
            "CDS": self.count(type="CDS"),
            "tRNA": self.count(type="tRNA"),
            "rRNA": self.count(type="rRNA"),
            "strand+": self.count(strand="+"),
            "strand-": self.count(strand="-"),
        }

        return stats

    def add(self, feature: Feature) -> Feature:
        """
        Add a Feature to the genome.
        """

        self.features.append(feature)

        return feature

    def remove(self, gene: str) -> int:
        """
        Remove all features matching a gene name.

        Returns
        -------
        int
            Number of removed features.
        """

        original = len(self.features)

        self.features = [
            feature
            for feature in self.features
            if feature.gene != gene
        ]

        return original - len(self.features)

    def sort(self) -> "Genome":
        """
        Sort features by genomic coordinates.
        """

        self.features.sort(
            key=lambda feature: (feature.start, feature.end)
        )

        return self