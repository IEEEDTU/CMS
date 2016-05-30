from django.db import models
from Course.models import *
from django.apps import apps


class CourseCurriculumManager(models.Manager):
    def addCourseCurriculum(self, request):
        """ add course curriculum """
        C = Course.objects.getCourseById(request)
        CC = CourseCurriculum(
            course=C,
            unit=request['unit'],
            description=request['description']
        )
        CC.save()
        return CC

    def editCourseCurriculum(self, request):
        """ edit course curriculum """
        C = Course.objects.get(courseId=request['courseId'])
        CC = CourseCurriculum.objects.get(course=C, unit=request['unit'])
        CC.description=request['description']
        CC.save()
        return CC

    def deleteCourseCurriculum(self, request):
        """ delete course curriculum """
        C = Course.objects.getCourseById(request)
        CC = CourseCurriculum.objects.get(course=C, unit=request['unit'])
        CC = CC.delete()
        return CC

    def getCourseCurriculum(self, request):
        """ get course curriculum on the basis of course and unit """
        C = Course.objects.getCourseById(request)
        CC = CourseCurriculum.objects.get(course=C, unit=request['unit'])
        return CC

    def retrieveCourseCurriculum(self, request):
        """ retrieve course curriculum on the basis of course """
        C = Course.objects.get(courseId=request['courseId'])
        CC = CourseCurriculum.objects.filter(course=C)
        return CC


class CourseCurriculum(models.Model):
    # Course
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=False)
    # Unit
    unit = models.PositiveIntegerField()
    # Description
    description = models.TextField()

    objects = CourseCurriculumManager()

    def __str__(self):
        return str(self.course)
