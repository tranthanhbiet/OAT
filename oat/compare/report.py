class ComparisonReport:
    """
    Stores the result of comparing two genomes.
    """

    def __init__(self):

        self.genome_a = None
        self.genome_b = None

        self.shared = []
        self.only_a = []
        self.only_b = []

    @property
    def similarity(self):

        total = (
            len(self.shared)
            + len(self.only_a)
            + len(self.only_b)
        )

        if total == 0:
            return 100.0

        return 100.0 * len(self.shared) / total

    def __repr__(self):

        return (
            f"ComparisonReport("
            f"shared={len(self.shared)}, "
            f"only_a={len(self.only_a)}, "
            f"only_b={len(self.only_b)})"
        )

    def __str__(self):

        lines = []

        lines.append("Genome Comparison")
        lines.append("=================")
        lines.append("")

        lines.append(f"Shared genes : {len(self.shared)}")
        lines.append(f"Only in A    : {len(self.only_a)}")
        lines.append(f"Only in B    : {len(self.only_b)}")
        lines.append(f"Similarity   : {self.similarity:.1f}%")

        if self.only_a:
            lines.append("")
            lines.append("Only in Genome A")
            lines.append("----------------")

            for gene in sorted(self.only_a):
                lines.append(f"- {gene}")

        if self.only_b:
            lines.append("")
            lines.append("Only in Genome B")
            lines.append("----------------")

            for gene in sorted(self.only_b):
                lines.append(f"- {gene}")

        return "\n".join(lines)