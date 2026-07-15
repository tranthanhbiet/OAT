import oat

from oat.merge.evidence import add_source


def test_consensus():

    g1 = oat.read(
        "examples/genbank/example.gb"
    )

    g2 = oat.read(
        "examples/genbank/example.gb"
    )

    g1 = add_source(g1, "GenBank")

    g2 = add_source(g2, "MITOS2")

    consensus = oat.merge_genomes([g1, g2])

    assert len(consensus.features) == 41

    assert consensus.features[0].confidence == 2

    assert len(consensus.sources) == 2