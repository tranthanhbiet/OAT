import oat


def run(args):

    from oat import read
    from oat.cli.errors import cli_error

    try:
        genome = read(args.input)

        print(genome.summary())

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