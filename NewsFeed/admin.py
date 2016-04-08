from django.contrib import admin
from NewsFeed.models import News,Notice,Announcements,Events
# Register your models here.
admin.site.register(News)
admin.site.register(Notice)
admin.site.register(Announcements)
admin.site.register(Events)