import oat


def test_validation():

    genome = oat.read(
        "examples/genbank/example.gb"
    )

    report = oat.validate(
        genome,
        expected_genes=[
            "cox1",
            "fake_gene",
        ],
    )

    assert len(report.errors) == 1

    assert report.errors[0].message == (
        "Missing gene: fake_gene"
    )