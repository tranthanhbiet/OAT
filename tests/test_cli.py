"""
Tests for the OAT command-line interface.
"""

from pathlib import Path
import subprocess


EXAMPLE = Path("examples/genbank/example.gb")


def run_oat(*args):
    """
    Run the OAT command and return the completed process.
    """
    return subprocess.run(
        ["oat", *args],
        capture_output=True,
        text=True,
    )


# ==========================================================
# Basic commands
# ==========================================================

def test_cli_version():
    """The --version option should execute successfully."""

    result = run_oat("--version")

    assert result.returncode == 0
    assert "OAT" in result.stdout


def test_cli_help():
    """The help page should list all available commands."""

    result = run_oat("--help")

    assert result.returncode == 0

    assert "summary" in result.stdout
    assert "validate" in result.stdout
    assert "compare" in result.stdout
    assert "export" in result.stdout


# ==========================================================
# Summary
# ==========================================================

def test_cli_summary():
    """The summary command should produce genome information."""

    result = run_oat(
        "summary",
        str(EXAMPLE),
    )

    assert result.returncode == 0

    assert "Organism" in result.stdout
    assert "Accession" in result.stdout
    assert "Length" in result.stdout


# ==========================================================
# Validation
# ==========================================================

def test_cli_validate():
    """Validation should pass for the example genome."""

    result = run_oat(
        "validate",
        str(EXAMPLE),
    )

    assert result.returncode == 0

    assert "Validation Report" in result.stdout
    assert "PASS" in result.stdout


# ==========================================================
# Comparison
# ==========================================================

def test_cli_compare():
    """Comparing a genome with itself should give 100% similarity."""

    result = run_oat(
        "compare",
        str(EXAMPLE),
        str(EXAMPLE),
    )

    assert result.returncode == 0

    assert "Genome Comparison" in result.stdout
    assert "100.0%" in result.stdout


# ==========================================================
# Export
# ==========================================================

def test_cli_export_fasta(tmp_path):
    """Export to FASTA."""

    outfile = tmp_path / "example.fa"

    result = run_oat(
        "export",
        str(EXAMPLE),
        str(outfile),
    )

    assert result.returncode == 0
    assert outfile.exists()


def test_cli_export_gff3(tmp_path):
    """Export to GFF3."""

    outfile = tmp_path / "example.gff3"

    result = run_oat(
        "export",
        str(EXAMPLE),
        str(outfile),
    )

    assert result.returncode == 0
    assert outfile.exists()


# ==========================================================
# Error handling
# ==========================================================

def test_cli_missing_file():
    """Missing input files should return an error."""

    result = run_oat(
        "summary",
        "does_not_exist.gb",
    )

    assert result.returncode != 0

    output = result.stdout + result.stderr

    assert "ERROR" in output
    assert "Input file not found" in output