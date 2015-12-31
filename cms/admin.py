from django.contrib import admin

# Register your models here.
from cms.models import Course
from cms.models import Address
from cms.models import Faculty
from cms.models import Name
from cms.models import Person
from cms.models import SpecializationField
from cms.models import Student

admin.site.register(Course)
admin.site.register(Address)
admin.site.register(Faculty)
admin.site.register(Name)
admin.site.register(Person)
admin.site.register(SpecializationField)
admin.site.register(Student)
