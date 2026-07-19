from pathlib import Path

from oat.export.fasta import FASTAExporter
from oat.export.gff3 import GFF3Exporter


EXPORTERS = {
    ".fa": FASTAExporter,
    ".fasta": FASTAExporter,
    ".gff": GFF3Exporter,
    ".gff3": GFF3Exporter,
}


def write(genome, filename):
    """
    Export a genome to the format inferred from the output filename extension.
    """

    suffix = Path(filename).suffix.lower()

    exporter_class = EXPORTERS.get(suffix)

    if exporter_class is None:
        raise ValueError(
            f"Unsupported output format: '{suffix}'. "
            f"Supported formats: {', '.join(sorted(EXPORTERS.keys()))}"
        )

    exporter = exporter_class()
    exporter.write(genome, filename)