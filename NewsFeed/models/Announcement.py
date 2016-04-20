from django.db import models
from Course.models import CourseGroup
import datetime


class AnnouncementManager(models.Manager):
    def addAnnouncement(self, request):
        """ adds new announcement """
        CG = CourseGroup.objects.getCourseGroup(request)
        A = Announcement(
            title=request['title'],
            content=request['content'],
            courseGroup=CG,
            dateAndTime=datetime.datetime.now()
        )
        A.save()
        return A

    def editAnnouncement(self, request):
        """ edit an existing announcement """
        """ note: courseGroup, dateAndTime is not editable """
        A = Announcement.objects.get(id=request['id'])
        A.title = request['title']
        A.content = request['content']
        A.save()
        return A

    def getAnnouncementById(self, request):
        """ get event details based on announcement id """
        A = Announcement.objects.get(id=request['id'])
        return A

    def retrieveAnnouncements(self, request):
        """ retrieve all announcements of a particular course group """
        CG = CourseGroup.objects.getCourseGroup(request)
        A = Announcement.objects.filter(courseGroup=CG)
        return A

    def deleteAnnouncement(self, request):
        """ deletes an existing announcement """
        A = Announcement.objects.get(id=request['id'])
        A = A.delete()
        return A

    def retrieveLatestAnnouncement(self, request):
        """ retrieves latest Announcement """
        """ criteria is to just return top 10 Announcement """
        lastTen = Announcement.objects.filter(date>=request['since']).order_by('-date')[:10]
        return lastTen

    def retrieveMoreAnnouncement(self, request):
        A = Announcement.objects.all()
        paginator = Paginator(A, request['rowsPerPage'])
    
        page = request['page']
        try:
            announcement = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            announcement = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            announcement = paginator.page(paginator.num_pages)
    
        return announcement


class Announcement(models.Model):
    # Title of announcement
    title = models.CharField(max_length=50, blank=False, null=False)
    # Content of the announcement
    content = models.CharField(max_length=500, blank=False, null=False)
    # CourseGroup Object from class CourseGroup
    courseGroup = models.ForeignKey(CourseGroup, on_delete=models.CASCADE, default=False)
    # Date and Time of the announcement(TIME FORMAT NOT IN IST)
    dateAndTime = models.DateTimeField(auto_now_add=False, auto_now=True)

    objects = AnnouncementManager()

    def __str__(self):
        return self.title

