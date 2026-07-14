from dataclasses import dataclass, field

from oat.models.feature import Feature


@dataclass
class FeatureBlock:
    """
    Raw feature block parsed from an annotation file.

    Internal parser object.
    """

    start: int
    end: int
    type: str

    qualifiers: dict = field(default_factory=dict)


def normalize_blocks(blocks):
    """
    Convert FeatureBlocks into OAT Feature objects.

    Consecutive gene + CDS/tRNA/rRNA blocks with identical
    coordinates are merged into one biological feature.
    """

    features = []

    i = 0

    while i < len(blocks):

        block = blocks[i]

        # -----------------------------
        # gene + biological feature
        # -----------------------------
        if (
            block.type == "gene"
            and i + 1 < len(blocks)
        ):

            next_block = blocks[i + 1]

            if (
                next_block.start == block.start
                and next_block.end == block.end
                and next_block.type in {"CDS", "tRNA", "rRNA"}
            ):

                feature = Feature()

                feature.type = next_block.type
                feature.start = block.start
                feature.end = block.end

                # copy gene qualifiers
                feature.gene = block.qualifiers.get("gene", "")
                feature.note = block.qualifiers.get("note", "")

                # copy biological qualifiers
                feature.product = next_block.qualifiers.get("product", "")
                feature.protein_id = next_block.qualifiers.get("protein_id", "")
                feature.anticodon = next_block.qualifiers.get("anticodon", "")
                feature.ec_number = next_block.qualifiers.get("EC_number", "")

                features.append(feature)

                i += 2
                continue

        # -----------------------------
        # standalone feature
        # -----------------------------
        feature = Feature()

        feature.type = block.type
        feature.start = block.start
        feature.end = block.end

        feature.gene = block.qualifiers.get("gene", "")
        feature.product = block.qualifiers.get("product", "")
        feature.protein_id = block.qualifiers.get("protein_id", "")
        feature.note = block.qualifiers.get("note", "")
        feature.anticodon = block.qualifiers.get("anticodon", "")
        feature.ec_number = block.qualifiers.get("EC_number", "")

        features.append(feature)

        i += 1

    return features