from django.db import models
from .Person import *
from Course.models import Degree
from Course.models import Branch
import datetime

class StudentManager(models.Manager):
	def addStudent(self,request):
		"""inserts person details in the database"""
		nameObjs = Name.objects.addName(request)
		addressObjs = Address.objects.addAddress(request)
		contactObjs = Mobile.objects.addContacts(request)
		degreeObj = Degree.objects.get(degreeCode = request['degreeCode'])
		
		S = Student(
			dtuRegId = request["dtuRegId"],
			name = nameObjs[0],
			permanentAdd = addressObjs[0],
			presentAdd = addressObjs[1],
			guardianAdd = addressObjs[2],
			personalMobile = contactObjs[0],
			alternativeMobile = contactObjs[1],
			personalEmail = request["personalEmail"],
			alternativeEmail = request["alternativeEmail"],
			dateOfBirth = request["dateOfBirth"],
			gender = request["gender"],
			category = request["category"],
			nationality = request["nationality"],
			religion = request["religion"],
			dormitory = request["dormitory"],
			fatherName = nameObjs[1],
			motherName = nameObjs[2],
			rollNo = request['rollNo'],
			branch = Branch.objects.get(branchCode = request['branchCode']),
			degree = degreeObj,
			admissionYear = request['admissionYear'],
			graduationYear = request['admissionYear'] + degreeObj.duration,
			password = request['password'],
		)
		S.save()
		return S
	def getStudentById(self,request):
		#To get the object of student by its dtuRegId
		S = Student.objects.get(dtuRegId = request["dtuRegId"])
		return S

class Student(Person):
	# Roll number
	rollNo = models.CharField(max_length=30, primary_key=False, blank=False, null=False)
	# Branch of the student
	branch = models.ForeignKey(Branch, on_delete = models.CASCADE, default=False)
	# Degree programme of the student
	degree = models.ForeignKey(Degree, on_delete = models.CASCADE, default=False)
	# Year of admission
	admissionYear = models.PositiveIntegerField()
	# Year of graduation
	graduationYear = models.PositiveIntegerField()
	# Library ID
	libraryId = models.CharField(max_length=30, blank=True, null=True)
	# Login's password
	password = models.CharField(max_length=100, blank=False, null=False)

	objects = StudentManager()
	
	def __str__(self):
		return self.rollNo + " - " + self.name