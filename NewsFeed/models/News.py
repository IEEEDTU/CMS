
from django.db import models
from Profiler.models import Faculty

class NewsManager(models.Manager):
	def addNews(self,request):
		publishedByObj = Faculty.getFacultyByFacultyId(request)

		N = News(
				headline = request['headline'],
				description = request['description'],
				image =  request['image'],
				link = request['url'],
				date = request['date'],
				publishedBy = publishedByObj
			)
		N.save()
		return N

	def getNewsById(self,request):
		"""get news details based on news id"""
		N = News.objects.get(id = request['id'])
		return N

	def retrieveProjects(self,request):
		pass

	def deleteProject(self, request):
		"""deletes news"""
		N = News.objects.get(request['id'])
		N = N.delete()
		return N


class News(models.Model):
	#Headline
	headline = models.CharField(max_length=100,null=False,blank=False)
	#Desciption
	description = models.CharField(max_length=4000,null=False,blank=False)
	#Image
	image = models.URLField(null=True, blank=True)
	#Link
	link = models.URLField(null=True, blank=True)
	#Date
	date = models.DateField(auto_now=False, auto_now_add=True)
	#Published By
	publishedBy = models.CharField(max_length=100,null=False,blank=False)

	objects = NewsManager()

	def __str__(self):
		return self.headline