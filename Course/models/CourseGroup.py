from django.db import models
from .Course import *
from .Group import *

class CourseGroup(models.Model):
    # Course
    course = models.ForeignKey(Course, on_delete = models.CASCADE, default=False)
    # Group
    group = models.ForeignKey(Group, on_delete = models.CASCADE, default=False)
	# Instructor
    #instructor = models.ForeignKey(Faculty,	on_delete = models.CASCADE)
    
    def __str__(self):
        return self.course + " - " + self.group