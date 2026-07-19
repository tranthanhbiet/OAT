from oat.export.base import BaseExporter


class FASTAExporter(BaseExporter):

    def write(self, genome, filename):

        with open(filename, "w") as out:

            header = genome.organism

            if genome.accession:

                header += f" [{genome.accession}]"

            out.write(f">{header}\n")

            seq = genome.sequence

            for i in range(0, len(seq), 60):

                out.write(seq[i:i+60] + "\n")