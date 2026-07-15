from oat.validation.report import ValidationReport


def check_overlaps(genome):
    """
    Detect overlapping genome features.
    """

    report = ValidationReport()

    features = sorted(
        genome.features,
        key=lambda f: f.start
    )

    for i in range(len(features) - 1):

        a = features[i]
        b = features[i + 1]

        if a.end >= b.start:

            overlap = a.end - b.start + 1

            report.add(
                "WARNING",
                (
                    f"Overlap: "
                    f"{a.gene} ({a.type}) "
                    f"and "
                    f"{b.gene} ({b.type}) "
                    f"overlap by {overlap} bp"
                )
            )

    return report