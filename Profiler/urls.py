from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^addStudent', views.addStudent, name='addStudent'),
	url(r'^editStudent', views.editStudent, name='editStudent'),
	url(r'^deleteStudent', views.deleteStudent, name='deleteStudent'),
	url(r'^retrieveProjects', views.retrieveProjects, name='retrieveProjects'),
	url(r'^addProject', views.addProject, name='addProject'),
	url(r'^getStudentByRollNo', views.getStudentByRollNo, name='getStudentByRollNo'),
	
	url(r'^addFaculty', views.addFaculty, name='addFaculty'),
	url(r'^editFaculty', views.editFaculty, name='editFaculty'),
	url(r'^deleteFaculty', views.deleteFaculty, name='deleteFaculty'),
	url(r'^getFacultyById', views.getFacultyById, name='getFacultyById'),
]
