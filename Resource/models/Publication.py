from django.db import models
from .Resource import *


class PublicationManager(models.Manager):
    def addPublication(self, request):
        """ add new publication """
        R = Resource.objects.addResource(request)
        P = Publication(
            resource=R,
            title=request['title'],
            authors=request['authors'],
            publicationDate=request['publicationDate'],
            organization=request['organization'],
            link=request['link']
        )
        P.save()
        return P

    def editPublication(self, request):
        """ edit existing publication """
        R = Resource.objects.editResource(request)
        P = Publication.objects.get(resource=R)
        P.title = request['title']
        P.authors = request['authors']
        P.publicationDate = request['publicationDate']
        P.organization = request['organization']
        P.link = request['link']
        P.save()
        return P

    def getDocumentById(self, request):
        """ get publication details on the basis of resource ID """
        R = Resource.objects.getResourceById(request)
        P = Publication.objects.get(resource=R)
        return P

    def retrievePublications(self, request):
        """ retrieve details of all the publications depending on the request """
        """ note: courseId is compulsory field; title, authors, organization, link are optional fields """
        R = Resource.objects.retrieveResources(request)
        P = Publication.objects.filter(pk__in=R)
        if 'title' in request.keys():
            P = P.objects.filter(title=request['title'])
        if 'authors' in request.keys():
            P = P.objects.filter(authors=request['authors'])
        if 'organization' in request.keys():
            P = P.objects.filter(organization=request['organization'])
        if 'link' in request.keys():
            P = P.objects.filter(link=request['link'])

        return P

    def deletePublication(self, request):
        """ deletes existing publication """
        R = Resource.objects.getResourceById(request)
        P = Publication.objects.get(resource=R)
        P.delete()
        R.delete()
        return P


class Publication(models.Model):
    # Resource
    resource = models.OneToOneField(Resource, on_delete=models.CASCADE, primary_key=True)
    # Title
    title = models.CharField(max_length=500, blank=False, null=False)
    # Authors
    authors = models.CharField(max_length=250)
    # Publication date
    publicationDate = models.DateField(editable=True, auto_now=False, auto_now_add=False)
    # Organization
    organization = models.CharField(max_length=100)
    # Link
    link = models.URLField()

    objects = PublicationManager()

    def __str__(self):
        return self.title + " - " + self.authors + " - " + self.publicationDate
