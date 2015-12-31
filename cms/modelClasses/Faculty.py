from django.db import models

class Faculty(models.Model):
	facultyId = models.CharField(max_length=50, blank=False, null=False)
	designation = models.CharField(max_length=50, blank=False, null=False)
	dateOfJoining = models.DateField()
	jobType = models.CharField(max_length=50, blank=False, null=False)
	# department = models.ForeignKey(
	# 	'department',
	# 	on_delete = models.CASCADE,
	# )
	dtuRegID = models.CharField(max_length=10,primary_key=True, blank=False, null=False)
	# field = models.ForeignKey(
	# 	'field',
	# 	on_delete=models.CASCADE,
	# )
	# salary = models.ForeignKey(
	# 	'salary',
	# 	on_delete=models.CASCADE,
	# )
	libraryId = models.CharField(max_length=30, blank=False, null=False)
	password = models.CharField(max_length=100, blank=False, null=False)

	def __str__(self):
		return self.facultyId