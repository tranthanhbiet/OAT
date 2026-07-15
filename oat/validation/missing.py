from oat.validation.report import ValidationReport


def check_missing(genome, expected_genes):
    """
    Check whether expected genes are present.

    Parameters
    ----------
    genome : Genome
    expected_genes : list[str]

    Returns
    -------
    ValidationReport
    """

    report = ValidationReport()

    observed = {
        feature.gene
        for feature in genome.features
        if feature.gene
    }

    for gene in expected_genes:

        if gene not in observed:

            report.add(
                "ERROR",
                f"Missing gene: {gene}"
            )

    return report