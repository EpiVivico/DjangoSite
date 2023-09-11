from projects.models import Project
from home.models import Portfolio

def deleteAllProjectInstances():
    Project.objects.all().delete()

def findProjectInstances():
    total = 0
    qs = Project.objects.all()
    for instance in qs:
        print(instance)


def findPortfolioInstances():
    total = 0
    qs = Portfolio.objects.all()
    for instance in qs:
        print(instance)

# deleteAllProjectInstances()
findProjectInstances()
findPortfolioInstances()