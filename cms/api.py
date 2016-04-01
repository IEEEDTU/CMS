from tastypie.resources import ModelResource
from cms.modelClasses.Course import Course as c
from tastypie.authorization import Authorization

class CourseResource(ModelResource):
    class Meta:
        queryset = c.objects.all()
        resource_name = 'course'
        allowed_methods = ['get', 'post', 'put']
        authorization = Authorization()