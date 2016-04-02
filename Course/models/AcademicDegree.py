from django.db import models

class DegreeManager(models.Manager):
	def addDegree(self, request):
		D = Degree(
			degreeCode = request['degreeCode'],
			degreeName = request['degreeName'],
			degreeType = request['degreeType'],
			duration = request['duration'],
			maxCredit = request['maxCredit'],
			annualFee = request['annualFee'],
			lateFine = request['lateFine'],
			admissionFee = request['admissionFee']
			)
		D.save()
		return D
	def getDegree(self, request):
		""" get the degree details using degreeCode"""
		D = Degree.objects.get(degreeCode = request['degreeCode'])
		return D
	def deleteDegree(seld, request):
		"""deletes any existing degree on the basis of degreeCode """
		D = Degree.objects.get(degreeCode = request['degreeCode'])
		D = D.delete()
		return D

class Degree(models.Model):
    # Degree code
    degreeCode = models.CharField(max_length=10)
    # Degree name
    degreeName = models.CharField(max_length=30)
    # Degree type
    degreeType = models.CharField(max_length=10)
    # Duration
    duration = models.PositiveIntegerField()
    # Maximum credits
    maxCredit = models.PositiveIntegerField()
    # Annual fee
    annualFee = models.DecimalField(max_digits=8, decimal_places=2)
    # Late submission fine
    lateFine = models.DecimalField(max_digits=8, decimal_places=2)
    # Admission fee
    admissionFee = models.DecimalField(max_digits=8, decimal_places=2)
    
    objects = DegreeManager()
    
    def __str__(self):
        return self.degreeCode + " - " + self.degreeName + " (" + self.degreeType + ")"
