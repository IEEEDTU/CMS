from django.db import models

class Group(models.Model):
	groupId = models.CharField(max_length=20, blank=False, null=False)
	semester = models.IntegerField()
	startRollNo = models.CharField(max_length=20, blank=False, null=False)
	endRollNo = models.CharField(max_length=20, blank=False, null=False)
	# branch = models.ForeignKey(
	# 	'Branch',
	# 	on_delete = models.CASCADE,
	# )
	strength = models.IntegerField()

	def __str__(self):
		return self.groupId