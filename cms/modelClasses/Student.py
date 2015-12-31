from django.db import models

class Student(models.Model):
	rollNo = models.CharField(max_length=30, blank=False, null=False)
	dtuRegId=models.CharField(max_length=10,primary_key=True, blank=False, null=False)
	# branch = models.ForeignKey(
	# 	'Branch',
	# 	on_delete = models.CASCADE,
	# )
	# degree = models.ForeignKey(
	# 	'Degree',
	# 	on_delete = models.CASCADE,
	# )
	admissionYear = models.IntegerField()
	passingYear = models.IntegerField()
	libraryId = models.CharField(max_length=30, blank=False, null=False)
	password = models.CharField(max_length=100, blank=False, null=False)

	def __str__(self):
		return self.dtuRegId