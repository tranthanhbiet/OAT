from oat.models.evidence import Evidence


def add_source(genome, source_name, version=""):
    """
    Add one evidence record to every feature
    in a genome.
    """

    # Remember where this genome came from
    genome.source = source_name

    for feature in genome.features:

        e = Evidence()

        e.source = source_name
        e.version = version

        feature.add_evidence(e)

    return genome