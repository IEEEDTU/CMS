from django.contrib import admin

# Register your models here.
from cms.models import Course
from cms.models import Address
from cms.models import Faculty
from cms.models import Name
from cms.models import Person
from cms.models import SpecializationField
from cms.models import Student
from cms.models import Batch
from cms.models import Group
from cms.models import CourseGroup
from cms.models import Score
from cms.models import Result


admin.site.register(Course)
admin.site.register(Address)
admin.site.register(Faculty)
admin.site.register(Name)
admin.site.register(Person)
admin.site.register(SpecializationField)
admin.site.register(Student)
admin.site.register(Batch)
admin.site.register(Group)
admin.site.register(CourseGroup)
admin.site.register(Score)
admin.site.register(Result)
