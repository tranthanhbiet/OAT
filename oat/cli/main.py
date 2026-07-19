import argparse

from oat import __version__

from oat.cli.summary import run as run_summary
from oat.cli.validate import run as run_validate
from oat.cli.compare import run as run_compare
from oat.cli.export import run as run_export


def main() -> None:
    """
    OAT command-line interface.
    """

    parser = argparse.ArgumentParser(
        prog="oat",
        description=(
            "Organelle Annotation Toolkit (OAT)\n\n"
            "A toolkit for parsing, validating, comparing, "
            "and exporting organelle genome annotations."
        ),
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"OAT {__version__}",
    )

    subparsers = parser.add_subparsers(
        dest="command",
        title="Available commands",
        metavar="<command>",
    )

    # ==========================================================
    # summary
    # ==========================================================

    summary = subparsers.add_parser(
        "summary",
        help="Summarize a genome annotation",
    )

    summary.add_argument(
        "input",
        help="Input annotation file",
    )

    # ==========================================================
    # validate
    # ==========================================================

    validate = subparsers.add_parser(
        "validate",
        help="Validate a genome annotation",
    )

    validate.add_argument(
        "input",
        help="Input annotation file",
    )

    # ==========================================================
    # compare
    # ==========================================================

    compare_cmd = subparsers.add_parser(
        "compare",
        help="Compare two genome annotations",
    )

    compare_cmd.add_argument(
        "input_a",
        help="First annotation file",
    )

    compare_cmd.add_argument(
        "input_b",
        help="Second annotation file",
    )

    # ==========================================================
    # export
    # ==========================================================

    export = subparsers.add_parser(
        "export",
        help="Export a genome annotation",
    )

    export.add_argument(
        "input",
        help="Input annotation file",
    )

    export.add_argument(
        "output",
        help="Output filename (format inferred from extension)",
    )

    # ==========================================================
    # Dispatch
    # ==========================================================

    args = parser.parse_args()

    if args.command == "summary":
        run_summary(args)
        return

    if args.command == "validate":
        run_validate(args)
        return

    if args.command == "compare":
        run_compare(args)
        return

    if args.command == "export":
        run_export(args)
        return

    parser.print_help()


if __name__ == "__main__":
    main()