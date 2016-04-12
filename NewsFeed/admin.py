from django.contrib import admin
from NewsFeed.models import News, Notice, Announcement, Event

# Register your models here.
admin.site.register(News)
admin.site.register(Notice)
admin.site.register(Announcement)
admin.site.register(Event)
