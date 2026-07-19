# OAT
## Organelle Annotation Toolkit

**OAT** is a modern Python toolkit for reading, validating, comparing, and exporting organelle genome annotations.

It provides both a reusable Python library and a command-line interface (CLI), making it suitable for bioinformatics pipelines, annotation quality control, comparative genomics, and future consensus annotation workflows.

---

## Features

Current features include:

- Read GenBank annotation files
- Read NCBI Feature Table (TBL) files
- Validate organelle genome annotations
- Compare multiple genome annotations
- Export annotations to FASTA
- Export annotations to GFF3
- Python API for workflow integration
- Command-line interface (CLI)
- Automated testing with pytest

---

## Installation

Clone the repository:

```bash
git clone https://github.com/<your_username>/OAT.git
cd OAT
```

Create or activate your Python environment, then install OAT in editable mode:

```bash
python -m pip install -e .
```

Verify the installation:

```bash
oat --version
```

Expected output:

```text
OAT 0.2.0
```

---

## Quick Start

### View a genome summary

```bash
oat summary examples/genbank/example.gb
```

Example output:

```text
Organism : Example species
Accession: XXXXXXXX
Length   : 23502 bp

CDS  : 14
tRNA : 25
rRNA : 2
Total: 41
```

---

### Validate a genome

```bash
oat validate examples/genbank/example.gb
```

---

### Compare two annotations

```bash
oat compare annotation1.gb annotation2.gb
```

---

### Export annotation

Export to FASTA:

```bash
oat export annotation.gb annotation.fa
```

Export to GFF3:

```bash
oat export annotation.gb annotation.gff3
```

---

# Python API

OAT can also be used directly in Python.

```python
import oat

genome = oat.read("example.gb")

report = oat.validate(genome)

oat.write(genome, "example.gff3")
```

---

# Supported Formats

## Import

| Format | Status |
|---------|:------:|
| GenBank | ✅ |
| NCBI Feature Table (TBL) | ✅ |
| GFF3 | 🚧 Planned |
| MITOS2 | 🚧 Planned |
| MFannot | 🚧 Planned |

---

## Export

| Format | Status |
|---------|:------:|
| FASTA | ✅ |
| GFF3 | ✅ |

---

# Testing

Run the complete test suite:

```bash
pytest
```

Current status:

```text
15 tests
15 passed
```

---

# Project Structure

```text
OAT/
│
├── oat/                Source code
├── tests/              Automated tests
├── examples/           Example datasets
├── README.md
├── pyproject.toml
└── LICENSE
```

---

# Roadmap

### Version 0.2

- Public Python API
- Command-line interface
- Validation framework
- Comparison framework
- FASTA export
- GFF3 export
- Automated testing

### Future development

- GFF3 parser
- MITOS2 parser
- MFannot parser
- Consensus annotation engine
- Evidence scoring
- Annotation reconciliation

---

# Citation

If you use OAT in your research, please cite the associated publication.

(Citation information will be added after publication.)

---

# License

This project is distributed under the LICENSE included with the repository.