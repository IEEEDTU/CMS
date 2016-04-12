from django.contrib import admin
from Course.models import Department, Laboratory, Degree, Batch, Branch, Group, Course, CourseGroup

# Register your models here.
admin.site.register(Department)
admin.site.register(Laboratory)
admin.site.register(Degree)
admin.site.register(Batch)
admin.site.register(Branch)
admin.site.register(Group)
admin.site.register(Course)
admin.site.register(CourseGroup)
