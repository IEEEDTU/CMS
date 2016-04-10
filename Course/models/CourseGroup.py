from django.db import models
from .Course import *
from .Group import *
#from Profiler.models import Faculty


class CourseGroup(models.Model):
    # Course
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=False)
    # Group
    group = models.ForeignKey(Group, on_delete=models.CASCADE, default=False)
    # Instructor
    instructor = models.ForeignKey('Profiler.Faculty', related_name="instructor", on_delete=models.CASCADE, default=False)

    def __str__(self):
        return self.course + " - " + self.group
