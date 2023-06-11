from .models import Project
def listProjects_resolver(obj, info):
    try:
        projects = [project.to_dict() for project in Project.query.all()]