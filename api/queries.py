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