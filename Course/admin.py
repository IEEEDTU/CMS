from django.contrib import admin
from Course.models import Degree,Batch,Branch,Course,CourseGroup,Department,Group,Laboratory
# Register your models here.
admin.site.register(Degree)
admin.site.register(Batch)
admin.site.register(Branch)
admin.site.register(Course)
admin.site.register(CourseGroup)
admin.site.register(Department)
admin.site.register(Group)
admin.site.register(Laboratory)