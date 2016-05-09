from django.contrib import admin
from Profiler.models import Person, Student, Faculty, Project, Field, Skill, StudentField, StudentSkill, FacultyField

# Register your models here.
#admin.site.register(Person)
admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Project)
admin.site.register(Field)
admin.site.register(Skill)
admin.site.register(StudentField)
admin.site.register(StudentSkill)
admin.site.register(FacultyField)