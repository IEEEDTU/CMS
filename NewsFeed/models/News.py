from django.db import models
from Profiler.models import *
from django.core.paginator import Paginator

class NewsManager(models.Manager):
    def addNews(self, request):
        """ adds new news """
        global obj
        if "rollNo" in request.keys():
            obj = Student.objects.getStudentByRollNo(request)
        elif "facultyId" in request.keys():
            obj = Faculty.objects.getFacultyByFacultyId(request)
        publishedBy = obj.name

        N = News(
            headline=request['headline'],
            description=request['description'],
            publishedBy=publishedBy
        )

        if "image" in request.keys():
            N.image = request['image']
        if "link" in request.keys():
            N.link = request['link']

        N.save()
        return N

    def editNews(self, request):
        """ edit the news details """
        """ only headline and description are editable """
        N = News.objects.get(id=request['id'])
        N.headline = request['headline']
        N.description = request['description']
        N.save()
        return N

    def getNewsById(self, request):
        """ get news details based on news id """
        N = News.objects.get(id=request['id'])
        return N

    def retrieveNews(self, request):
        """ retrieve all the news """
        """ optional fields: headline, date, publishedBy """
        N = News.objects.all()
        if 'headline' in request.keys():
            N = N.filter(headline=request['headline'])
        if 'date' in request.keys():
            N = N.filter(date=request['date'])
        if 'publishedBy' in request.keys():
            N = N.filter(publishedBy=request['publishedBy'])

        return N

    def retrieveLatestNews(self, request):
        """ retrieves latest news """
        """ criteria is to just return top 10 news """
        lastTen = News.objects.filter(date__gte = request['since']).order_by('-date')[:10]
        return lastTen

    def retrieveMoreNews(self, request):
        N = News.objects.all()
        paginator = Paginator(N, request['rowsPerPage'])
    
        page = request['pageNo']
        try:
            news = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            news = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            news = paginator.page(paginator.num_pages)
    
        return news

    def deleteNews(self, request):
        """ deletes an existing news """
        N = News.objects.get(id=request['id'])
        N = N.delete()
        return N


class News(models.Model):
    # Headline
    headline = models.CharField(max_length=250, null=False, blank=False)
    # Description
    description = models.CharField(max_length=4000, null=False, blank=False)
    # Image
    image = models.URLField(null=True, blank=True)
    # Link
    link = models.URLField(null=True, blank=True)
    # Date
    date = models.DateField(auto_now=False, auto_now_add=True)
    # Published By
    publishedBy = models.ForeignKey(Name, related_name="news_published_by", null=False, blank=False)

    objects = NewsManager()

    def __str__(self):
        return self.headline
