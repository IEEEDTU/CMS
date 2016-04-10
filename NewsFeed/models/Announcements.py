from django.db import models
from Course.models import *
import datetime

class AnnouncementManager(models.Manager):
    def addAnnouncement(self, request):
        """ adds new announcement """
        CG = CourseGroup.objects.get(id = request['id'])
        A = Announcement(
            title = request['title'],
            content = request['content'],
            courseGroup = CG,
            dateAndTime = datetime.datetime.now()
        )
        A.save()
        return A

    def editAnnouncement(self, request):
        """ edit an existing announcement """
        """ note: courseGroup, dateAndTime is not editable """
        A = Announcement.objects.get(id = request['id'])
        A.title = request['title']
        A.content = request['content']
        A.save()
        return A

    def deleteAnnouncement(self, request):
        """ deletes an existing announcement """
        A = Announcement.objects.get(id = request['id'])
        A = A.delete()
        return A

class Announcement(models.Model):
    # Title of announcement
    title = models.CharField(max_length=50, blank=False, null=False)
    # Content of the announcement
    content = models.CharField(max_length=500, blank=False, null=False)
    # CourseGroup Object from class CourseGroup
    courseGroup = models.ForeignKey(CourseGroup, on_delete = models.CASCADE, default=False)
    # Date and Time of the announcement(TIME FORMAT NOT IN IST)
    dateAndTime = models.DateTimeField(auto_now_add=False, auto_now=True)

    objects = AnnouncementManager()

    def __str__(self):
        return self.title

dr={
    'title':"Bla Bla Announcement",
    'content':"This is a Bla Bla event",
    'courseGroup':1
}