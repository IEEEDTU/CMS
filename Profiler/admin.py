from django.contrib import admin
from Profiler.models import Faculty,Person,Project,Field,Student
# Register your models here.

admin.site.register(Faculty)
# admin.site.register(Person)
admin.site.register(Project)
admin.site.register(Field)
admin.site.register(Student)