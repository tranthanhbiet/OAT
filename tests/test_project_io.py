from oat.models.project import Project
from oat.project_io import save_project, load_project

# Create a project
project = Project()
project.name = "Test Project"
project.genome.name = "Macrocheira_kaempferi"

# Save
save_project(project, "test.oat")

# Load
loaded = load_project("test.oat")

# Verify
assert loaded.name == project.name
assert loaded.version == project.version
assert loaded.genome.name == project.genome.name
assert loaded.genome.topology == project.genome.topology

print("PASS")