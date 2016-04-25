from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^addResource', views.addResource, name='addResource'),
    url(r'^editResource', views.editResource, name='editResource'),
    url(r'^deleteResource', views.deleteResource, name='deleteResource'),
    url(r'^retrieveResources', views.retrieveResources, name='retrieveResources'),
]
