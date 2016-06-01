from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^addNews', views.addNews, name='addNews'),
    url(r'^editNews', views.editNews, name='editNews'),
    url(r'^deleteNews', views.deleteNews, name='deleteNews'),
    url(r'^retrieveLatestNews', views.retrieveLatestNews, name='retrieveLatestNews'),
    url(r'^retrieveMoreNews', views.retrieveMoreNews, name='retrieveMoreNews'),
    url(r'^getNewsById', views.getNewsById, name='getNewsById'),
    
    url(r'^addNotice', views.addNotice, name='addNotice'),
    url(r'^editNotice', views.editNotice, name='editNotice'),
    url(r'^deleteNotice', views.deleteNotice, name='deleteNotice'),
    url(r'^retrieveLatestNotices', views.retrieveLatestNotices, name='retrieveLatestNotices'),
    url(r'^retrieveMoreNotices', views.retrieveMoreNotices, name='retrieveMoreNotices'),
    
    url(r'^addEvent', views.addEvent, name='addEvent'),
    url(r'^editEvent', views.editEvent, name='editEvent'),
    url(r'^deleteEvent', views.deleteEvent, name='deleteEvent'),
    url(r'^retrieveLatestEvents', views.retrieveLatestEvents, name='retrieveLatestEvents'),
    url(r'^retrieveMoreEvents', views.retrieveMoreEvents, name='retrieveMoreEvents'),
    url(r'^getEventById', views.getEventById, name='getEventById'),
    
    url(r'^addAnnouncement', views.addAnnouncement, name='addAnnouncement'),
    url(r'^editAnnouncement', views.editAnnouncement, name='editAnnouncement'),
    url(r'^deleteAnnouncement', views.deleteAnnouncement, name='deleteAnnouncement'),
    url(r'^retrieveLatestAnnouncements', views.retrieveLatestAnnouncements, name='retrieveLatestAnnouncements'),
    url(r'^retrieveMoreAnnouncements', views.retrieveMoreAnnouncements, name='retrieveMoreAnnouncements'),
]
