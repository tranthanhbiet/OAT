def parse_metadata(lines):
    """
    Parse basic metadata from a GenBank file.

    Returns
    -------
    dict
    """

    metadata = {
        "definition": "",
        "accession": "",
        "organism": "",
        "length": 0,
        "topology": "",
    }

    for line in lines:

        # LOCUS
        if line.startswith("LOCUS"):

            fields = line.split()

            if len(fields) >= 3:
                metadata["length"] = int(fields[2])

            if len(fields) >= 6:
                metadata["topology"] = fields[5].lower()

        # DEFINITION
        elif line.startswith("DEFINITION"):

            metadata["definition"] = line[12:].strip()

        # ACCESSION
        elif line.startswith("ACCESSION"):

            metadata["accession"] = line[12:].strip()

        # ORGANISM
        elif line.startswith("  ORGANISM"):

            metadata["organism"] = line[12:].strip()

    return metadata