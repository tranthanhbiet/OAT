import oat
from oat.validation import validate


def run(args):

    from oat import read
    from oat.validation import validate
    from oat.cli.errors import cli_error

    try:
        genome = read(args.input)

        report = validate(genome)

        print(report)

    except FileNotFoundError:

        cli_error(
            "Input file not found",
            f"Cannot open:\n\n{args.input}",
        )

    except Exception as e:

        cli_error(
            "Unexpected error",
            str(e),
        )