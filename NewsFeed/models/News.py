from django.db import models
from Profiler.models import *


class NewsManager(models.Manager):
    def addNews(self, request):
        """ adds new news """
        global obj
        if "rollNo" in request.keys():
            obj = Student.objects.getStudentByRollNo(request)
        elif "facultyId" in request.keys():
            obj = Faculty.objects.getFacultyByFacultyId(request)
        publishedBy = obj.name

        N = News(
            headline=request['headline'],
            description=request['description'],
            publishedBy=publishedBy
        )

        if "image" in request.keys():
            N.image=request['image']
        if "link" in request.keys():
            link=request['link']

        N.save()
        return N

    def getNewsById(self, request):
        """ get news details based on news id """
        N = News.objects.get(id=request['id'])
        return N

    def retrieveNews(self, request):
        pass

    def deleteNews(self, request):
        """ deletes an existing news """
        N = News.objects.get(id=request['id'])
        N = N.delete()
        return N


class News(models.Model):
    # Headline
    headline = models.CharField(max_length=250, null=False, blank=False)
    # Desciption
    description = models.CharField(max_length=4000, null=False, blank=False)
    # Image
    image = models.URLField(null=True, blank=True)
    # Link
    link = models.URLField(null=True, blank=True)
    # Date
    date = models.DateField(auto_now=False, auto_now_add=True)
    # Published By
    publishedBy = models.ForeignKey(Name, related_name="news_published_by", null=False, blank=False)

    objects = NewsManager()

    def __str__(self):
        return self.headline

