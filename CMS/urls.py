"""CMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url,include
from django.contrib import admin

from Course import urls as course_urls
from NewsFeed import urls as newsfeed_urls
from Profiler import urls as profiler_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^course/',include(course_urls)),
    url(r'^newsfeed/',include(newsfeed_urls)),
    url(r'^profiler/',include(profiler_urls)),
]
