from django.db import models
from Profiler.models import Student


class ProjectManager(models.Manager):
    def addProject(self, request):
        """ adds new project """
        S = Student.objects.getStudentByRegIdOrRollNo(request)
        P = Project(
            student=S,
            title=request['title'],
            description=request['description'],
            highlight=request['highlight'],
            startDate=request['startDate'],
            endDate=request['endDate'],
            projectType=request['projectType'],
            teamSize=request['teamSize']
        )
        P.save()
        return P

    def editProject(self, request):
        """ edit the project """
        P = Project.objects.get(id=request['id'])

        P.title=request['title']
        P.description=request['description']
        P.highlight=request['highlight']
        P.startDate=request['startDate']
        P.endDate=request['endDate']
        P.projectType=request['projectType']
        P.teamSize=request['teamSize']

        P.save()
        return P

    def getProjectById(self, request):
        """ get project details based on project id """
        P = Project.objects.get(id=request['id'])
        return P

    def retrieveProjects(self, request):
        """ retrieve projects of student depending on the request """
        """ note: student is must """
        """ other optional attributes: projectType, title """
        S = Student.objects.getStudentByRegIdOrRollNo(request)
        P = Project.objects.filter(student=S)

        if 'projectType' in request.keys():
            P = P.filter(projectType=request['projectType'])
        if 'title' in request.keys():
            P = P.filter(title=request['title'])

        return P

    def deleteProject(self, request):
        """ deletes existing project """
        P = Project.objects.get(id=request['id'])
        P = P.delete()
        return P


class Project(models.Model):
    # Options for projects
    MAJOR = 'MAJ'
    MINOR = 'MIN'
    RESEARCH = 'RES'
    INTERN = 'INT'
    TRAINING = 'TRA'
    OTHER = 'OTH'
    PROJECT_CHOICES = (
        (MAJOR, 'Major'),
        (MINOR, 'Minor'),
        (RESEARCH, 'Research'),
        (INTERN, 'Intern'),
        (TRAINING, 'Training'),
        (OTHER, 'Other'))

    # Student
    student = models.ForeignKey(Student, on_delete=models.CASCADE, default=False)
    # Title of Project
    title = models.CharField(max_length=500, blank=False, null=False)
    # Description of Project
    description = models.CharField(max_length=5000, blank=False, null=False)
    # Highlight of Project
    highlight = models.CharField(max_length=500, blank=False, null=False)
    # Start Date of Project
    startDate = models.DateField(null=False, blank=False)
    # End Date of Project
    endDate = models.DateField()
    # Type of Project
    projectType = models.CharField(max_length=20, choices=PROJECT_CHOICES, default=OTHER)
    # Size of Team
    teamSize = models.PositiveIntegerField()

    objects = ProjectManager()

    def __str__(self):
        return self.title
