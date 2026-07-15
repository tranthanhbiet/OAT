import oat


def test_read_genbank():

    genome = oat.read(
        "examples/genbank/example.gb"
    )

    assert genome.organism == "Pseudosuberites sp. CY-2021"

    assert genome.accession == "MN547324"

    assert len(genome.features) == 41