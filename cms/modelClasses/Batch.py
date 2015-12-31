from django.db import models

class Batch(models.Model):
	batchId = models.CharField(max_length=20, blank=False, null=False)
	batchType = models.CharField(max_length=5, blank=False, null=False)
	# degree = models.ForeignKey(
	# 	'Degree',
	# 	on_delete = models.CASCADE,
	# )
	# dept = models.ForeignKey(
	# 	'Department',
	# 	on_delete = models.CASCADE,
	# )
	strength = models.IntegerField()

	def __str__(self):
		return self.batchId