from oat.compare.report import ComparisonReport


def compare(genome_a, genome_b):
    """
    Compare two genomes by gene names.
    """

    report = ComparisonReport()

    report.genome_a = genome_a
    report.genome_b = genome_b

    genes_a = {
        feature.gene
        for feature in genome_a.features
        if feature.gene
    }

    genes_b = {
        feature.gene
        for feature in genome_b.features
        if feature.gene
    }

    report.shared = sorted(genes_a & genes_b)
    report.only_a = sorted(genes_a - genes_b)
    report.only_b = sorted(genes_b - genes_a)

    return report