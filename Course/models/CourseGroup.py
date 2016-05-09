from django.apps import apps
from django.db import models
from .Course import *
from .Group import *
# from Profiler.models import Faculty


class CourseGroupManager(models.Manager):
    def addCourseGroup(self, request):
        """ add a course group """
        C = Course.objects.getCourseById(request)
        G = Group.objects.getGroupByIdAndCode(request)
        F = apps.get_model('Profiler','Faculty').objects.get(facultyId=request["facultyId"])
        CG = CourseGroup(
            course=C,
            group=G,
            instructor=F
        )
        CG.save()
        return CG

    def editCourseGroup(self, request):
        """ edit course group """
        F = apps.get_model('Profiler','Faculty').objects.get(facultyId=request["facultyId"])
        C = Course.objects.getCourseById(request)
        G = Group.objects.getGroupByIdAndCode(request)
        CG = CourseGroup.objects.get(course=C, group=G)
        CG.instructor = F
        CG.save()
        return CG

    def deleteCourseGroup(self, request):
        """ delete course group """
        C = Course.objects.getCourseById(request)
        G = Group.objects.getGroupById(request)
        CG = CourseGroup.objects.get(course=C, group=G)
        CG = CG.delete()
        return CG

    def getCourseGroup(self, request):
        """ get course group on the basis of course and group """
        C = Course.objects.getCourseById(request)
        G = Group.objects.getGroupByIdAndCode(request)
        CG = CourseGroup.objects.get(course=C, group=G)
        return CG

    def getCourseGroupsByCourse(self, request):
        """ get course groups on the basis of course """
        C = Course.objects.getCourseById(request)
        CG = CourseGroup.objects.filter(course=C)
        return CG

    def getCourseGroupsByGroup(self, request):
        """ get course groups on the basis of group """
        G = Group.objects.getGroupByIdAndCode(request)
        CG = CourseGroup.objects.filter(group=G)
        return CG

    def getCoursesByGroup(self, request):
        """ get courses on the basis of group """
        G = Group.objects.getGroupByIdAndCode(request)
        CG = CourseGroup.objects.filter(group=G)
        ids = []
        for obj in CG:
            ids.append(obj.course.courseId)
        C = Course.objects.filter(courseId__in=ids)
        return C

    def getGroupsByCourse(self, request):
        """ get groups on the basis of course """
        C = Course.objects.getCourseById(request)
        CG = CourseGroup.objects.filter(course=C)
        ids = []
        for obj in CG:
            ids.append(obj.group.pk)
        G = Group.objects.filter(pk__in=ids)
        return G


class CourseGroup(models.Model):
    # Course
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=False)
    # Group
    group = models.ForeignKey(Group, on_delete=models.CASCADE, default=False)
    # Instructor
    instructor = models.ForeignKey('Profiler.Faculty', on_delete=models.CASCADE)

    objects = CourseGroupManager()

    def __str__(self):
        return str(self.course) + " - " + str(self.group)
