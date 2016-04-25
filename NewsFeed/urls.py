from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^addNews', views.addNews, name='addNews'),
    url(r'^editNews', views.editNews, name='editNews'),
    url(r'^deleteNews', views.deleteNews, name='deleteNews'),
    url(r'^retrieveLatestNews', views.retrieveLatestNews, name='retrieveLatestNews'),
    url(r'^retrieveMoreNews', views.retrieveMoreNews, name='retrieveMoreNews'),
    
    url(r'^addNotice', views.addNotice, name='addNotice'),
    url(r'^editNotice', views.editNotice, name='editNotice'),
    url(r'^deleteNotice', views.deleteNotice, name='deleteNotice'),
    url(r'^retrieveLatestNotice', views.retrieveLatestNotice, name='retrieveLatestNotice'),
    url(r'^retrieveMoreNotice', views.retrieveMoreNotice, name='retrieveMoreNotice'),
    
    url(r'^addEvent', views.addEvent, name='addEvent'),
    url(r'^editEvent', views.editEvent, name='editEvent'),
    url(r'^deleteEvent', views.deleteEvent, name='deleteEvent'),
    url(r'^retrieveLatestEvent', views.retrieveLatestEvent, name='retrieveLatestEvent'),
    url(r'^retrieveMoreEvent', views.retrieveMoreEvent, name='retrieveMoreEvent'),
    
    url(r'^addAnnouncement', views.addAnnouncement, name='addAnnouncement'),
    url(r'^editAnnouncement', views.editAnnouncement, name='editAnnouncement'),
    url(r'^deleteAnnouncement', views.deleteAnnouncement, name='deleteAnnouncement'),
    url(r'^retrieveLatestAnnouncement', views.retrieveLatestAnnouncement, name='retrieveLatestAnnouncement'),
    url(r'^retrieveMoreAnnouncement', views.retrieveMoreAnnouncement, name='retrieveMoreAnnouncement'),
]
