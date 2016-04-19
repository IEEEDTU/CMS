from django.db import models
from .Course import *
from .Group import *
# from Profiler.models import Faculty


class CourseGroupManager(models.Manager):
    def getCourseGroup(self, request):
        """ get course group on the basis of course and group """
        C = Course.objects.get(courseId=request['courseId'])
        G = Group.objects.get(groupId=request['groupId'])
        CG = CourseGroup.objects.get(course=C, group=G)
        return CG


class CourseGroup(models.Model):
    # Course
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=False)
    # Group
    group = models.ForeignKey(Group, on_delete=models.CASCADE, default=False)
    # Instructor
    instructor = models.ForeignKey('Profiler.Faculty', related_name="instructor", on_delete=models.CASCADE,
                                   default=False)

    objects = CourseGroupManager()

    def __str__(self):
        return self.course + " - " + self.group
