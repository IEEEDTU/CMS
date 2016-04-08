from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^addCourse', views.addCourse, name='addCourse'),
]