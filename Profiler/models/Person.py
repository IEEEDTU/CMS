from django.db import models

class NameManager(models.Manager):
	def addName(self, request):
		"""add names in the database"""
		nameObjs = []
		nameObjs.append(Name(
			fname = request["name"]["fname"],
			mname = request["name"]["mname"],
			lname = request["name"]["lname"],
			preferredName = request["name"]["preferredName"]))
		nameObjs.append( Name(
			fname = request["fatherName"]["fname"],
			mname = request["fatherName"]["mname"],
			lname = request["fatherName"]["lname"],
			preferredName = request["fatherName"]["preferredName"]))
		nameObjs.append( Name(
			fname = request["motherName"]["fname"],
			mname = request["motherName"]["mname"],
			lname = request["motherName"]["lname"],
			preferredName = request["motherName"]["preferredName"]))
		
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
	preferredName = models.CharField(max_length=100, blank=False, null=False, unique=True)
	
	objects = NameManager()
	
	def __str__(self):
		return self.preferredName


class AddressManager(models.Manager):
	def __eq__(self, obj1, obj2, keys):
		"""compares two objects on the basis of keys given"""
		dict1 = {k:obj1.__dict__[k] for k in keys}
		dict2 = {k:obj2.__dict__[k] for k in keys}
		return dict1==dict2

	def addAddress(self, request):
		""" add addresses in the database """
		addressObjs = []
		addressObjs.append( Address(
			locality = request['permanentAdd']['locality'],
			city = request['permanentAdd']['city'],
			state = request['permanentAdd']['state'],
			country = request['permanentAdd']['country'],
			pincode = request['permanentAdd']['pincode']))
		addressObjs.append( Address(
			locality = request['presentAdd']['locality'],
			city = request['presentAdd']['city'],
			state = request['presentAdd']['state'],
			country = request['presentAdd']['country'],
			pincode = request['presentAdd']['pincode']))
		addressObjs.append( Address(
			locality = request['guardianAdd']['locality'],
			city = request['guardianAdd']['city'],
			state = request['guardianAdd']['state'],
			country = request['guardianAdd']['country'],
			pincode = request['guardianAdd']['pincode']))

		objs = []
		# 1st argument should be saved as it is
		addressObjs[0].save()
		objs.append(addressObjs[0])
		
		# keys to be used for comparison
		keys = ["locality", "city", "state", "country", "pincode"]
		
		# checking 2nd argument
		# if it is same as 1st then just append 1st argument in the object list 
		# else save new item and append that in the object list
		if(self.__eq__(addressObjs[0],addressObjs[1],keys)):
			objs.append(addressObjs[0])
		else:
			addressObjs[1].save()
			objs.append(addressObjs[1])

		# checking 3rd argument
		# if it is same as 1st or 2nd then just append respective argument in the object list 
		# else save new item and append that in the object list
		if(self.__eq__(addressObjs[0],addressObjs[2],keys)):
			objs.append(addressObjs[0])
		elif(self.__eq__(addressObjs[1],addressObjs[2],keys)):
			objs.append(addressObjs[1])
		else:
			addressObjs[2].save()
			objs.append(addressObjs[2])    

		return objs

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
		contactObjs.append( Mobile(
			countryCode = request["personalMobile"]["countryCode"],
			mobileNum = request["personalMobile"]["mobileNum"]))
		contactObjs.append( Mobile(
			countryCode = request["alternativeMobile"]["countryCode"],
			mobileNum = request["alternativeMobile"]["mobileNum"]))
		
		for contact in contactObjs:
			contact.save()
		
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
