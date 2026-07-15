from copy import deepcopy

from oat.consensus.consensus import ConsensusGenome


def merge_genomes(genomes):
    """
    Merge genomes by gene name.

    The first occurrence of a gene becomes the
    representative feature.
    Evidence from later genomes is appended.
    """

    consensus = ConsensusGenome()

    merged = {}

    for genome in genomes:

        for feature in genome.features:

            gene = feature.gene.strip()

            if gene == "":
                continue

            if gene not in merged:

                merged[gene] = deepcopy(feature)

            else:

                merged[gene].evidence.extend(
                    feature.evidence
                )

        # Record evidence sources
        for feature in genome.features:

            for evidence in feature.evidence:

                consensus.add_source(
                    evidence.source
                )

    consensus.features = list(merged.values())

    return consensus