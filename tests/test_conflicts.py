import oat

from oat.merge.evidence import add_source
from oat.consensus.compare import compare_genomes


def test_presence_conflict():

    g1 = add_source(
        oat.read("examples/genbank/example.gb"),
        "GenBank",
    )

    g2 = add_source(
        oat.read("examples/genbank/example.gb"),
        "MITOS2",
    )

    # Remove one gene
    assert g2.remove("cox1") == 1

    comparison = compare_genomes([g1, g2])

    conflicts = comparison.find_conflicts()

    assert len(conflicts) == 1
    assert conflicts[0].gene == "cox1"
    assert conflicts[0].kind == "presence"