from oat.models.genome import Genome


class Project:
    """
    Represents an OAT project.
    """

    def __init__(self):
        self.name = ""
        self.version = "0.1"
        self.genome = Genome()
        self.notes = ""