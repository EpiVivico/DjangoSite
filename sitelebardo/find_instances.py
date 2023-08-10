from projects.models import Project

def deleteAllProjectInstances():
    Project.objects.all().delete()

def findProjectInstances():
    total = 0
    qs = Project.objects.all()
    for instance in qs:
        print(instance)

deleteAllProjectInstances()
findProjectInstances()