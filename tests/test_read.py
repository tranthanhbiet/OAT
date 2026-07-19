from pathlib import Path

import oat


EXAMPLE = Path("examples/genbank/example.gb")


def test_read_genbank():

    genome = oat.read(EXAMPLE)

    assert genome is not None
    assert genome.length > 0
    assert genome.organism is not None