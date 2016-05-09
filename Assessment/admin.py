from django.contrib import admin
from Assessment.models import Score, Result, Assignment, AssignmentResponse

# Register your models here.
admin.site.register(Score)
admin.site.register(Result)
admin.site.register(Assignment)
admin.site.register(AssignmentResponse)
