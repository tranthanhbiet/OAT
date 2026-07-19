from oat.consensus.comparison import FeatureComparison
from oat.consensus.genome_comparison import GenomeComparison


def compare_genomes(genomes):
    """
    Compare multiple Genome objects by gene name.

    Parameters
    ----------
    genomes : list[Genome]

    Returns
    -------
    GenomeComparison
    """

    comparison = GenomeComparison()

    # Collect all gene names
    genes = set()

    for genome in genomes:
        for feature in genome.features:
            if feature.gene:
                genes.add(feature.gene)

    # Build one FeatureComparison per gene
    for gene in sorted(genes):

        fc = FeatureComparison(gene)

        for genome in genomes:

            source = getattr(genome, "source", "Unknown")

            feature = genome.find(gene)

            fc.add(source, feature)

        comparison.add(fc)

    return comparison