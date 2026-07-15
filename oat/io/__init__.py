from pathlib import Path

from oat.parsers.genbank import parse_genbank
from oat.parsers.tbl import parse_tbl


def read(filename):
    """
    Read a genome annotation file.

    Supported formats
    -----------------
    .gb
    .gbk
    .tbl
    """

    suffix = Path(filename).suffix.lower()

    if suffix in {".gb", ".gbk"}:
        return parse_genbank(filename)

    if suffix == ".tbl":
        return parse_tbl(filename)

    raise ValueError(
        f"Unsupported file format: {suffix}"
    )