from django.db import models
from Profiler.models import Student

class ProjectManager(models.Manager):
    def addProject(self, request):
        """ adds new project """
        studentObj = Student.objects.getStudentByRegId(request)
        P = Project(
            student=studentObj,
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

    def getProjectById(self, request):
        """ get project details based on project id """
        P = Project.objects.get(id=request['id'])
        return P

    def retrieveProjects(self, request):
        """ retrieve IDs of all the projects depending on the request """
        """ note: student is must """
        """ other optional attributes: projectType, startDate """
        S = Student.objects.getStudentByRegId(request)
        objList = Project.objects.filter(student=S)

        if 'projectType' in request.keys():
            objList = objList.filter(projectType=request['projectType'])

        idList = []
        for obj in objList:
            idList.append(obj.id)
        return idList

    def deleteProject(self, request):
        """ deletes existing project """
        P = Project.objects.get(id=request['id'])
        P = P.delete()
        return P


class Project(models.Model):
    # Options for projects
    MAJOR = 'MJ'
    MINOR = 'MI'
    RESEARCH = 'RS'
    OTHER = 'OT'
    PROJECT_CHOICES = (
        (MAJOR, 'Major'),
        (MINOR, 'Minor'),
        (RESEARCH, 'Research'),
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
