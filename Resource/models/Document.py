from django.db import models
from .Resource import *


class DocumentManager(models.Manager):
    def addDocument(self, request):
        """ add new document """
        R = Resource.objects.addResource(request)
        D = Document(
            resource=R,
            documentType=request['documentType'],
            source=request['source']
        )
        D.save()
        return D

    def editDocument(self, request):
        """ edit existing document """
        R = Resource.objects.editResource(request)
        D = Document.objects.get(resource=R)
        D.documentId = request['documentId']
        D.documentType = request['documentType']
        D.source = request['source']
        D.save()
        return D

    def getDocumentById(self, request):
        """ get document details on the basis of resource ID """
        R = Resource.objects.getResourceById(request)
        D = Document.objects.get(resource=R)
        return D

    def retrieveDocuments(self, request):
        """ retrieve details of all the documents depending on the request """
        """ note: courseId is compulsory field; document type, source are optional fields """
        R = Resource.objects.retrieveResources(request)
        D = Document.objects.filter(pk__in=R)
        if 'documentType' in request.keys():
            D = D.objects.filter(documentType=request['documentType'])
        if 'source' in request.keys():
            D = D.objects.filter(source=request['source'])

        return D

    def deleteDocument(self, request):
        """ deletes existing document """
        R = Resource.objects.getResourceById(request)
        D = Document.objects.get(resource=R)
        D.delete()
        R.delete()
        return D


class Document(models.Model):
    WORD_DOCUMENT = 0
    TEXT_FILE = 1
    PRESENTATION = 2
    PDF = 3
    IMAGE = 4
    OTHER = 5
    DOCUMENT_TYPE_CHOICES = (
        (WORD_DOCUMENT, 'Word Document'), (TEXT_FILE, 'Text File'), (PRESENTATION, 'Presentation'), (PDF, 'PDF'), (IMAGE, 'Image'), (OTHER, 'Other'))

    # Resource
    resource = models.OneToOneField(Resource, on_delete=models.CASCADE, primary_key=True)
    # Type
    documentType = models.PositiveIntegerField(choices=DOCUMENT_TYPE_CHOICES, blank=False, null=False)
    # Source
    source = models.URLField(null=False, blank=False)

    objects = DocumentManager()

    def __str__(self):
        return self.source + " - " + str(self.documentType)
