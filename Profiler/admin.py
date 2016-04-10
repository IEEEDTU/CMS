from django.contrib import admin
from Profiler.models import Person, Student, Faculty, Project, Field, Skill

# Register your models here.
#admin.site.register(Person)
admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Project)
admin.site.register(Field)
admin.site.register(Skill)
