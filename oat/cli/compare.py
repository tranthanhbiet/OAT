import oat
from oat.compare import compare


def run(args):

    from oat import read
    from oat.compare import compare
    from oat.cli.errors import cli_error

    try:
        genome1 = read(args.input_a)
        genome2 = read(args.input_b)

        report = compare(genome1, genome2)

        print(report)

    except FileNotFoundError:

        cli_error(
            "Input file not found",
            "One or more input files could not be opened.",
        )

    except Exception as e:

        cli_error(
            "Unexpected error",
            str(e),
        )