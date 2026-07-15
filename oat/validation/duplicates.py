from collections import Counter

from oat.validation.report import ValidationReport


def check_duplicates(genome):
    """
    Check for duplicated gene names.

    Parameters
    ----------
    genome : Genome

    Returns
    -------
    ValidationReport
    """

    report = ValidationReport()

    genes = [
        feature.gene
        for feature in genome.features
        if feature.gene
    ]

    counts = Counter(genes)

    for gene, count in counts.items():

        if count > 1:

            report.add(
                "WARNING",
                f"Duplicate gene: {gene} ({count} copies)"
            )

    return report