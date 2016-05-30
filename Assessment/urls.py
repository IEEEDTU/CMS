from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^getAssignmentByCode', views.getAssignmentByCode, name='getAssignmentByCode'),
    url(r'^retrieveAssignments', views.retrieveAssignments, name='retrieveAssignments'),

]
