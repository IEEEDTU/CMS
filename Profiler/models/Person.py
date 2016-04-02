from django.db import models

class NameManager(models.Manager):
	"""add names in the database"""
	def addName(self, request):
		nameObjs = []
		nameObjs[0] = Name(
			fname = request["name"][0],
			mname = request["name"][1],
			lname = request["name"][2],
			preferredName = request["name"][3])
		nameObjs[1] = Name(
			fname = request["fatherName"][0],
			mname = request["fatherName"][1],
			lname = request["fatherName"][2],
			preferredName = request["motherName"][3])
		nameObjs[2] = Name(
			fname = request["motherName"][0],
			mname = request["motherName"][1],
			lname = request["motherName"][2],
			preferredName = request["motherName"][3])
		
		for name in nameObjs:
			name.save()
			
		return nameObjs

class Name(models.Model):
	# First Name
	fname = models.CharField(max_length=100, blank=False, null=False)
	# Middle Name
	mname = models.CharField(max_length=100, blank=True, null=True)
	# Last Name
	lname = models.CharField(max_length=100, blank=True, null=True)
	# Preferred Name
	preferredName = models.CharField(max_length=100, blank=False, null=False)
	
	objects = NameManager()
	
	def __str__(self):
		return self.preferredName

class AddressManager(models.Manager):
	def addAddress(self, request):
		A = []
		for i in range(0,3):
			A[i] = Address(
				locality = request['locality'][i],
				city = request['city'][i],
				state = request['state'][i],
				country = request['country'][i],
				pincode = request['pincode'][i]
				)
			A[i].save
		return A

class Address(models.Model):
	# Locality/Street/Area
	locality = models.CharField(max_length=100, blank=False, null=False)
	# City
	city = models.CharField(max_length=50, blank=False, null=False)
	# State
	state = models.CharField(max_length=50, blank=False, null=False)
	# Country
	country = models.CharField(max_length=50, blank=False, null=False)
	# PIN Code
	pincode = models.PositiveIntegerField()

	objects = AddressManager()
	
	def __str__(self):
		return self.locality + "," + self.city + "," + self.state + "," + self.country

class MobileManager(models.Manager):
	def addContacts(self, request):
		"""add contact numbers in the database"""
		contactObjs = []
		for i in range(0,3):
			contactObjs[i] = Mobile(
				countryCode = request[countryCode][i],
				mobileNum = request[mobileNum][i]
				)
			contactObjs[i].save()
		return contactObjs
	

class Mobile(models.Model):
	# Country Code
	countryCode = models.PositiveIntegerField(blank=False, null=False)
	# Mobile Number
	mobileNum = models.PositiveIntegerField(blank=False, null=False)

	objects = MobileManager()
	
	def __str__(self):
		return str(self.countryCode) + "-" + str(self.mobileNum)

class Person(models.Model):
	# DTU Registration ID
	dtuRegId = models.CharField(max_length=10, primary_key=True, blank=False, null=False)
	# Person's Name
	name = models.ForeignKey(Name, related_name="%(class)s_name", on_delete=models.CASCADE, default=False)
	# Permanent Address
	permanentAdd = models.ForeignKey(Address, related_name="%(class)s_permanent_address", on_delete=models.CASCADE, default=False)
	# Present Address
	presentAdd = models.ForeignKey(Address, related_name="%(class)s_present_address", on_delete=models.CASCADE, default=False)
	# Guardian Address
	guardianAdd = models.ForeignKey(Address, related_name="%(class)s_guardian_address", on_delete=models.CASCADE, default=False)
	# Personal Contact Number
	personalMobile = models.ForeignKey(Mobile, related_name="%(class)s_personal_mobile", on_delete=models.CASCADE, default=False)
	# Alternative Contact Number
	alternativeMobile = models.ForeignKey(Mobile, related_name="%(class)s_alternative_mobile", on_delete=models.CASCADE, default=False)
	# Personal Email Address
	personalEmail = models.EmailField(blank=False, null=False, default=False)
	# Alternative Email Address
	alternativeEmail = models.EmailField(default=False)
	# Date of Birth
	dateOfBirth = models.DateField(auto_now_add=False, auto_now=False, default=False)
	# Gender
	gender = models.CharField(max_length=1, blank=False, null=False)
	# Category (E.g.: SC, ST, OBC, PD)
	category = models.CharField(max_length=3, blank=False, null=False)
	# Nationality
	nationality = models.CharField(max_length=50, blank=False, null=False)
	# Religion
	religion = models.CharField(max_length=50, blank=False, null=False)
	# Dormitory
	dormitory= models.BooleanField(default=False)
	# Father's Name
	fatherName = models.ForeignKey(Name, related_name="%(class)s_father_name", on_delete=models.CASCADE, default=False)
	# Mother's Name
	motherName = models.ForeignKey(Name, related_name="%(class)s_mother_name", on_delete=models.CASCADE, default=False)
	# Photograph
	photo = models.BinaryField()
	# Signature
	signature = models.BinaryField()
	
	def __str__(self):
		return self.dtuRegId + " - " + self.name
	
	class Meta:
		abstract = True

n = {'name':['Vaibhav', 'xyz', 'sawhney', 'pinky'],
	'fatherName':['Anil','xyz','sawhney', 'papa'],
	'motherName':['Sushil','xyz','sawhney', 'mum']
	}
	