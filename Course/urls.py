from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^addCourse', views.addCourse, name='addCourse'),
    url(r'^retrieveCourses', views.retrieveCourses, name='retrieveCourses'),
    url(r'^getCourseById', views.getCourseById, name='getCourseById'),
    url(r'^retrieveDegrees', views.retrieveDegrees, name='retrieveDegrees'),
    url(r'^getDegreeByCodeAndType', views.getDegreeByCodeAndType, name='getDegreeByCodeAndType'),
    url(r'^retrieveBranches', views.retrieveBranches, name='retrieveBranches'),
    url(r'^getBranchByCode', views.getBranchByCode, name='getBranchByCode'),
    url(r'^retrieveBatches', views.retrieveBatches, name='retrieveBatches'),
    url(r'^getBatchById', views.getBatchById, name='getBatchById'),
    # url(r'^retrieveCourseGroups', views.retrieveCourseGroups, name='retrieveCourseGroups'),
]
