from projects.models import Project

def findProjectInstances():
    total = 0
    qs = Project.objects.all()
    for instance in qs:
        print(instance)

findProjectInstances()