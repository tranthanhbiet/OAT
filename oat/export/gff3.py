from oat.export.base import BaseExporter


class GFF3Exporter(BaseExporter):
    """
    Export a Genome to GFF3 format.
    """

    def write(self, genome, filename):

        with open(filename, "w", encoding="utf-8") as out:

            out.write("##gff-version 3\n")

            seqid = genome.accession or "Genome"

            for feature in genome.features:

                attributes = []

                if feature.gene:
                    attributes.append(f"ID={feature.gene}")
                    attributes.append(f"Name={feature.gene}")

                if feature.product:
                    attributes.append(
                        f"product={feature.product}"
                    )

                attr = ";".join(attributes)

                out.write(
                    "\t".join([
                        seqid,
                        "OAT",
                        feature.type,
                        str(feature.start),
                        str(feature.end),
                        ".",
                        feature.strand,
                        ".",
                        attr,
                    ])
                    + "\n"
                )