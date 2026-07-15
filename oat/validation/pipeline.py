from oat.validation.report import ValidationReport
from oat.validation.missing import check_missing
from oat.validation.duplicates import check_duplicates
from oat.validation.overlaps import check_overlaps


def validate(genome, expected_genes=None):
    """
    Run all validation checks on a genome.

    Parameters
    ----------
    genome : Genome
    expected_genes : list[str] | None

    Returns
    -------
    ValidationReport
    """

    report = ValidationReport()

    # Missing genes
    if expected_genes is not None:
        r = check_missing(genome, expected_genes)
        report.issues.extend(r.issues)

    # Duplicate genes
    r = check_duplicates(genome)
    report.issues.extend(r.issues)

    # Coordinate overlaps
    r = check_overlaps(genome)
    report.issues.extend(r.issues)

    return report