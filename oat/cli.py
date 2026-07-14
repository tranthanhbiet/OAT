import typer

app = typer.Typer(
    help="OAT (Organelle Annotation Toolkit)"
)


@app.command()
def version():
    """
    Show OAT version.
    """
    typer.echo("OAT version 0.1.0")


@app.command()
def init():
    """
    Initialize a new OAT project.
    """
    typer.echo("Initializing a new OAT project...")


if __name__ == "__main__":
    app()