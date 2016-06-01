from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^getAssignmentByCode', views.getAssignmentByCode, name='getAssignmentByCode'),
    url(r'^getAssignmentsByCourse', views.getAssignmentsByCourse, name='getAssignmentsByCourse'),
    url(r'^retrieveAssignments', views.retrieveAssignments, name='retrieveAssignments'),
    url(r'^retrieveAssignmentByBranch', views.retrieveAssignmentByBranch, name='retrieveAssignmentByBranch'),
    url(r'^retrieveAssignmentResponsesByStudent', views.retrieveAssignmentResponses, name='retrieveAssignmentResponses'),
    url(r'^getResultsByStudent', views.getResultsByStudent, name='getResultsByStudent'),

]
