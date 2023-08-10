from projects.models import Project

p1 = Project(
    title='My First Project',
    description='A web development project.',
    technology='Django',
    image='img/key.jpg'
)
p1.save()

p2 = Project(
    title='My Second Project',
    description='Another web development project.',
    technology='Flask',
    image='img/gaming.jpg'
)
p2.save()


p3 = Project(
    title='My Third Project',
    description='A final development project.',
    technology='Django',
    image='img/purple.jpg'
)
p3.save()