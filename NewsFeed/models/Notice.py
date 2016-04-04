# Subject, issuing authority, issue date, file , degree , branch , department
from django.db import models
from Profiler.models import Faculty,Student
from Course.models import Degree,Branch,Department

class NoticeManager(models.Manager):
	def addNotice(self,request):
		degreeObj = Degree.getDegreeByCodeAndType(request)
		branchObj = Branch.getBranchByCode(request)
		departmentObj = Department.objects.get(deptId= request['deptId'])

		N = Notice(
			subject = request['subject'],
			issuingAuthority = request['issuingAuthority'],
			issueDate = request['issueDate'],
			fileLink = request['fileLink'],
			degree = degreeObj,
			branch = branchObj,
			department = departmentObj,
		)
		N.save()
		return N

	def getNoticeById(self,request):
		"""get notice details based on notice id"""
		N = Notice.objects.get(id = request['id'])
		return N

	def retrieveNoticeById(self,request):
		pass

	def deleteNotice(self,request):
		"""deletes notice"""
		N = Notice.objects.get(request['id'])
		N = N.delete()
		return N



class Notice(models.Model):

	#Subject
	subject  = models.CharField(max_length=150, blank=False, null=False)
	#IssuingAuthority
	issuingAuthority = models.CharField(max_length=150, blank=False, null=False)
	#Issue date
	issueDate = models.DateTimeField(auto_now=False, auto_now_add=True)
	#Link of the file from DropBox
	fileLink = models.URLField(null=True, blank=True)
	#degree
	degree = models.ForeignKey(Degree, on_delete = models.CASCADE, default=False)
	#branch
	branch = models.ForeignKey(Department, on_delete = models.CASCADE, default=False)
	#department
	department = models.ForeignKey(Student, on_delete = models.CASCADE, default=False)

	objects = NoticeManager()

	def __str__(self):
		return self.subject