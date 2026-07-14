import json


def project_to_dict(project):
    """
    Convert a Project object into a Python dictionary.
    """

    return {
        "format_version": "1.0",
        "project": {
            "name": project.name,
            "version": project.version,
            "notes": project.notes,
        },
        "genome": {
            "name": project.genome.name,
            "organism": project.genome.organism,
            "sequence": project.genome.sequence,
            "topology": project.genome.topology,
            "genetic_code": project.genome.genetic_code,
        },
        "features": [],
    }

def save_project(project, filename):
    """
    Save a Project object to an OAT (.oat) file.
    """

    data = project_to_dict(project)

    with open(filename, "w", encoding="utf-8") as outfile:
        json.dump(data, outfile, indent=4)


from oat.models.project import Project


def load_project(filename):
    """
    Load an OAT (.oat) file into a Project object.
    """

    with open(filename, "r", encoding="utf-8") as infile:
        data = json.load(infile)

    project = Project()

    project.name = data["project"]["name"]
    project.version = data["project"]["version"]
    project.notes = data["project"]["notes"]

    project.genome.name = data["genome"]["name"]
    project.genome.organism = data["genome"]["organism"]
    project.genome.sequence = data["genome"]["sequence"]
    project.genome.topology = data["genome"]["topology"]
    project.genome.genetic_code = data["genome"]["genetic_code"]

    return project
