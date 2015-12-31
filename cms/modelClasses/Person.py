from django.db import models

# class PersonManager(models.Manager):
# 	def addPerson(self,req):
# 		self.dtuRegId = req['dtuRegId']
# 		self.personalMobile = req['personalMobile']
# 		self.alternativeMobile = req['alternativeMobile']
# 		self.personalEmail = req['personalEmail']
# 		self.alternativeEmail = req['alternativeEmail']
# 		self.dateOfBirth = req['dateOfBirth']
# 		self.gender = req['gender']
# 		self.category = req['category']
# 		self.nationality = req['nationality']
# 		self.religion = req['religion']
# 		self.dormitory = req['dormitory']
# 		self.photo = req['photo']
# 		self.signature = req['s']

class Person(models.Model):
	dtuRegId=models.CharField(max_length=10,primary_key=True, blank=False, null=False)
	# name=models.ForeignKey(
	# 	'name',
	# 	on_delete=models.CASCADE,
	# )
	# permanentAdd=models.ForeignKey(
	# 	'permanentAdd',
	# 	on_delete=models.CASCADE,
	# )
	# presentAdd=models.ForeignKey(
	# 	'presentAdd',
	# 	on_delete=models.CASCADE,
	# )
	# guardianAdd=models.ForeignKey(
	# 	'guardianAdd',
	# 	on_delete=models.CASCADE,
	# )
	personalMobile = models.IntegerField()
	alternativeMobile = models.IntegerField()
	personalEmail = models.EmailField()
	alternativeEmail = models.EmailField()
	dateOfBirth = models.DateField(auto_now_add=True,auto_now=False)
	gender = models.CharField(max_length=1, blank=False, null=False)
	category = models.CharField(max_length=3, blank=False, null=False)
	nationality = models.CharField(max_length=50, blank=False, null=False)
	religion = models.CharField(max_length=50, blank=False, null=False)
	dormitory= models.BooleanField()
	# fatherName = ForeignKey(
	# 	'fatherName',
	# 	on_delete=models.CASCADE,
	# )
	# motherName =models.ForeignKey(
	# 	'motherName',
	# 	on_delete=models.CASCADE,
	# )
	photo = models.BinaryField()
	signature = models.BinaryField()


	def __str__(self):
		return self.dtuRegId
