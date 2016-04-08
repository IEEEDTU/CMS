from django.db import models
from Course.models import *
import datetime

class AnnouncementsManager(models.Manager):
    def addAnnouncement(self,request):
        D = Degree.objects.get(degreeCode = request['degreeCode'], degreeType = request['degreeType'])
        B = Branch.objects.getBranchByCode(request)

        #To be edited after making CourseGroup

        #Cg = CourseGroup.objects.get()

        C = Course.objects.get(courseId = request["courseId"])

        A = Announcements(
            title = request['title'],
            content = request['content'],
            degree = D,
            branch = B,
            course = C,
            dateAndTime = datetime.datetime.now()
        )

        A.save()
        return A

    def editAnnouncement(self,request):
        #We will take Announcement Id in request to edit it
        A = Announcements.objects.get(id = request['id'])
        A.title = request['title']
        A.content = request['content']
        A.degree = Degree.objects.get(degreeCode = request['degreeCode'], degreeType = request['degreeType'])
        A.branch = Branch.objects.getBranchByCode(request)

        #To be edited after making CourseGroup

        #A.courseGroup = CourseGroup.objects.get()

        A.course = Course.objects.get(courseId = request["courseId"])
        A.dateAndTime = datetime.datetime.now()
        A.save()
        return A

    def deleteAnnouncement(self,request):
        A = Announcements.objects.get(id = request['id'])
        A = A.delete()
        return A

class Announcements(models.Model):
    #Title of announcement
    title = models.CharField(max_length=50, blank=False, null=False)
    #Content of the announcement
    content = models.CharField(max_length=500, blank=False, null=False)
    #Degree Object from class Degree
    degree = models.ForeignKey(Degree, on_delete = models.CASCADE, default=False)
    #Branch Object from class Branch
    branch = models.ForeignKey(Branch, on_delete = models.CASCADE, default=False)
    #CourseGroup Object from class CourseGroup
#    courseGroup = models.ForeignKey(CourseGroup, on_delete = models.CASCADE, default=False)
    #Course Object from class Course
    course = models.ForeignKey(Course, on_delete = models.CASCADE, default=False)
    #Date and Time of the announcement(TIME FORMAT NOT IN IST)
    dateAndTime = models.DateTimeField(auto_now_add=False, auto_now=True)

    objects = AnnouncementsManager()

    def __str__(self):
        return self.title

dr={
    'title':"Bla Bla Announcement",
    'content':"This is a Bla Bla event",
    'degreeCode':"BTECH",
    'degreeType':"Regular",
    'branchCode':"SE",
    'courseId':"SE202"
}
drEdit={
    'id':"1",
    'title':"Results Out",
    'content':"Results are out for SEM V",
    'degreeCode':"BTECH",
    'degreeType':"Regular",
    'branchCode':"SE",
    'courseId':"SE202"
}
d={
    'id':"1"
}