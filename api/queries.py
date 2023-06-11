from ariadne import convert_kwargs_to_snake_case
from .models import Project

def listProjects_resolver(obj, info):
    try:
        projects = [project.to_dict() for project in Project.query.all()]
        print(projects)
        payload = {
            "success": True,
            "projects" : projects
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }    
    return payload    

@convert_kwargs_to_snake_case
def getProject_resolver(obj, info, id):
    try:
        project = Project.query.get(id)
        payload = {
            "success": True,
            "project": project.to_dict()
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": ["Project item matching {id} not found"]
        }
    return payload        