def summary(consensus):
    """
    Return a text summary of a consensus genome.
    """

    high = 0
    medium = 0
    low = 0

    lines = []

    lines.append("Consensus Summary")
    lines.append("=" * 40)
    lines.append("")

    lines.append(f"Sources : {len(consensus.sources)}")
    lines.append(f"Features: {len(consensus.features)}")
    lines.append("")

    lines.append("Gene\tConfidence\tLevel")

    for feature in consensus.features:

        lines.append(
            f"{feature.gene}\t"
            f"{feature.confidence}\t"
            f"{feature.confidence_level}"
        )

        if feature.confidence_level == "High":
            high += 1
        elif feature.confidence_level == "Medium":
            medium += 1
        else:
            low += 1

    lines.append("")
    lines.append("-" * 40)
    lines.append(f"High   : {high}")
    lines.append(f"Medium : {medium}")
    lines.append(f"Low    : {low}")

    return "\n".join(lines)