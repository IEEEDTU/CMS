from django.db import models
from .Resource import *


class WebLinkManager(models.Manager):
    def addWebLink(self, request):
        """ add new web link """
        R = Resource.objects.addResource(request)
        W = WebLink(
            resource=R,
            link=request['link']
        )
        W.save()
        return W

    def editWebLink(self, request):
        """ edit existing web link """
        R = Resource.objects.editResource(request)
        W = WebLink.objects.get(resource=R)
        W.link = request['link']
        W.save()
        return W

    def getWebLinkById(self, request):
        """ get web link details on the basis of resource ID """
        R = Resource.objects.getResourceById(request)
        W = WebLink.objects.get(resource=R)
        return W

    def retrieveWebLinks(self, request):
        """ retrieve details of all the web links depending on the request """
        """ note: courseId is compulsory field; link is optional field """
        R = Resource.objects.retrieveResources(request)
        W = WebLink.objects.filter(pk__in=R)
        if 'link' in request.keys():
            W = W.filter(link=request['link'])

        return W

    def deleteWebLink(self, request):
        """ deletes existing web link """
        R = Resource.objects.getResourceById(request)
        W = WebLink.objects.get(resource=R)
        W.delete()
        R.delete()
        return W


class WebLink(models.Model):
    # Resource
    resource = models.OneToOneField(Resource, on_delete=models.CASCADE, primary_key=True)
    # Link
    link = models.URLField(null=False, blank=False)

    objects = WebLinkManager()

    def __str__(self):
        return self.link
