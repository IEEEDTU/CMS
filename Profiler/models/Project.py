"""
title
description
highlight
startdate
end date
type
team size
"""

from django.db import models
from Course.models import Student

class ProjectManager(models.Manager):
	def addProject(self,request):
		"""Adds New Project"""
		studentObj = Student.objects.getStudentByRegId(request)
		P = Project(
				student = studentObj,
				title = request['title'],
				description = request['description'],
				highlight = request['highlight'],
				startDate = request['startDate'],
				endDate = request['endDate'],
				projectType = request['projectType'],
				teamSize = request['teamSize']
			)
		P.save()
		return P

	def getProjectById(self,request):
		"""get project details based on project id"""
		P = Project.objects.get(id = request['id'])
		return P

	def retrieveProjects(self,request):
		""" retrieve IDs of all the projects depending on the request """
        """ note: student is must """
        """ other optional attributes: projectType , startDate """
        S = Student.objects.getStudentByRegId(request)
        objList = Project.objects.filter(student=S)

        if projectType in request.keys():
        	objList = objList.filter(projectType = request['projectType'])

        idList = []
        for obj in objList:
            idList.append(obj.id)
        return idList

	def deleteProject(self, request):
		"""deletes project"""
		P = Project.objects.get(request['id'])
		P = P.delete()
		return S

class Project(models.Model):

	#Add Options for Projects Here
	MAJOR = 'MJ'
	MINOR = 'MN'
	SIDE = 'SD'
	PROJECT_CHOICES = (
		(MAJOR,'Major'),
		(MINOR,'Minor'),
		(SIDE,'Side'),
	)

	#Student
	student = models.ForeignKey(Student, on_delete = models.CASCADE, default=False)
	#Title of Project
	title = models.CharField(max_length=100, blank=False, null=False)
	#Description of Project
	description = models.CharField(max_length=250, blank=False, null=False)
	#Highlight of Project
	highlight = models.CharField(max_length=100, blank=False, null=False)
	#Start Date of Project
	startDate = models.DateField()
	#End Date of Project
	endDate = models.DateField()
	#Type of Project
	projectType = models.CharField(max_length=2,
								   choices = PROJECT_CHOICES,
								   default = MAJOR)
	#Size of Team
	teamSize = models.PositiveIntegerField()

	objects = ProjectManager()
    
    def __str__(self):
        return self.title