from django.contrib import admin
from Profiler.models import Faculty,Person,Project,SpecializationField,Student
# Register your models here.

admin.site.register(Faculty)
admin.site.register(Person)
admin.site.register(Project)
admin.site.register(SpecializationField)
admin.site.register(Student)