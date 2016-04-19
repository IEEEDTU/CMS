from django.db import models
from Course.models import Course
from Profiler.models import Faculty
#from Resource.models import Book, Document, Publication, WebLink
import datetime

class ResourceManager(models.Manager):
    def addResource(self, request):
        """ add new resource """
        C = Course.objects.getCourseById(request)
        F = Faculty.objects.getFacultyByRegId(request)
        R = Resource(
            course=C,
            updatedBy=F
        )
        R.save()
        return R

    def editResource(self, request):
        """ edit existing resource """
        """ note: course is not editable """
        F = Faculty.objects.getFacultyByRegId(request)
        R = Resource.objects.get(pk=request['resourceId'])
        R.updatedBy = F
        R.updatedOn = datetime.datetime.now()
        R.save()
        return R

    def getResourceById(self, request):
        """ get resource by id """
        R = Resource.objects.get(pk=request['resourceId'])
        return R

    def retrieveResources(self, request):
        """ retrieve details of all the resources on the basis of course """
        C = Course.objects.getCourseById(request)
        R = Resource.objects.filter(course=C)
        return R

    def deleteResource(self, request):
        """ deletes existing resource """
        R = Resource.objects.get(pk=request['resourceId'])
        R.delete()
        return R


class Resource(models.Model):
    # Course
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=False)
    # Date of update
    updatedOn = models.DateTimeField(auto_now=True)
    # Updated by
    updatedBy = models.ForeignKey(Faculty, on_delete=models.CASCADE, default=False)

    objects = ResourceManager()

    def __str__(self):
        return str(self.course)