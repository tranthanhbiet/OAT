import oat


def test_read_tbl():

    genome = oat.read(
        "examples/tbl/example.tbl"
    )

    assert len(genome.features) == 41

    assert genome.features[0].gene == "cox1"

    assert genome.features[0].type == "CDS"