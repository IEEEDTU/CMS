from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^addCourse', views.addCourse, name='addCourse'),
    url(r'^retrieveCourses', views.retrieveCourses, name='retrieveCourses'),
    url(r'^retrieveOddCourses', views.retrieveOddCourses, name='retrieveOddCourses'),
    url(r'^retrieveEvenCourses', views.retrieveEvenCourses, name='retrieveEvenCourses'),
    url(r'^getCourseById', views.getCourseById, name='getCourseById'),
    
    url(r'^addDegree', views.addDegree, name='addDegree'),
    url(r'^editDegree', views.editDegree, name='editDegree'),
    url(r'^deleteDegree', views.deleteDegree, name='deleteDegree'),
    url(r'^retrieveDegrees', views.retrieveDegrees, name='retrieveDegrees'),
    url(r'^getDegreeByCodeAndType', views.getDegreeByCodeAndType, name='getDegreeByCodeAndType'),
    
    url(r'^addBranch', views.addBranch, name='addBranch'),
    url(r'^editBranch', views.editBranch, name='editBranch'),
    url(r'^deleteBranch', views.deleteBranch, name='deleteBranch'),
    url(r'^retrieveBranches', views.retrieveBranches, name='retrieveBranches'),
    url(r'^getBranchByCode', views.getBranchByCode, name='getBranchByCode'),
    
    url(r'^addBatch', views.addBatch, name='addBatch'),
    url(r'^editBatch', views.editBatch, name='editBatch'),
    url(r'^deleteBatch', views.deleteBatch, name='deleteBatch'),
    url(r'^retrieveBatches', views.retrieveBatches, name='retrieveBatches'),
    url(r'^getBatchById', views.getBatchById, name='getBatchById'),
    
    url(r'^addCourseGroup', views.addCourseGroup, name='addCourseGroup'),
    url(r'^editCourseGroup', views.editCourseGroup, name='editCourseGroup'),
    url(r'^deleteCourseGroup', views.deleteCourseGroup, name='deleteCourseGroup'),
    url(r'^getInstructorDetails', views.getInstructorDetails, name='getInstructorDetails'),
    url(r'^retrieveCourseGroups', views.retrieveCourseGroups, name='retrieveCourseGroups'),
    
    url(r'^addDepartment', views.addDepartment, name='addDepartment'),
    url(r'^editDepartment', views.editDepartment, name='editDepartment'),
    url(r'^deleteDepartment', views.deleteDepartment, name='deleteDepartment'),
    url(r'^retrieveDepartments', views.retrieveDepartments, name='retrieveDepartments'),
    
    url(r'^addGroup', views.addGroup, name='addGroup'),
    url(r'^editGroup', views.editGroup, name='editGroup'),
    url(r'^deleteGroup', views.deleteGroup, name='deleteGroup'),
    url(r'^retrieveGroups', views.retrieveGroups, name='retrieveGroups'),

    url(r'^addCourseCurriculum', views.addCourseCurriculum, name='addCourseCurriculum '),
    url(r'^editCourseCurriculum', views.editCourseCurriculum, name='editCourseCurriculum '),
    url(r'^deleteCourseCurriculum', views.deleteCourseCurriculum, name='deleteCourseCurriculum'),
    url(r'^getCourseCurriculum', views.getCourseCurriculum, name='getCourseCurriculum'),
    url(r'^retrieveCourseCurriculum', views.retrieveCourseCurriculum, name='retrieveCourseCurriculum'),

]
