import oat


def test_statistics():

    genome = oat.read(
        "examples/genbank/example.gb"
    )

    stats = genome.statistics()

    assert stats["features"] == 41
    assert stats["CDS"] == 14
    assert stats["tRNA"] == 25
    assert stats["rRNA"] == 2