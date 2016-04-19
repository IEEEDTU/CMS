from django.db import models
from .Resource import *


class BookManager(models.Manager):
    def addBook(self, request):
        """ add new book """
        R = Resource.objects.addResource(request)
        B = Book(
            resource=R,
            bookName=request['bookName'],
            authors=request['authors'],
            edition=request['edition'],
            publisher=request['publisher'],
            bookType=request['bookType']
        )
        B.save()
        return B

    def editBook(self, request):
        """ edit existing book """
        R = Resource.objects.editResource(request)
        B = Book.objects.get(resource=R)
        B.bookName = request['bookName']
        B.authors = request['authors']
        B.edition = request['edition']
        B.publisher = request['publisher']
        B.bookType = request['bookType']
        B.save()
        return B

    def getBookById(self, request):
        """ get book details on the basis of resource ID """
        R = Resource.objects.getResourceById(request)
        B = Book.objects.get(resource=R)
        return B

    def retrieveBooks(self, request):
        """ retrieve details of all the books depending on the request """
        """ note: courseId is compulsory field; book name, book type, authors, publisher are optional fields """
        R = Resource.objects.retrieveResources(request)
        B = Book.objects.filter(pk__in=R)
        if 'bookName' in request.keys():
            B = B.objects.filter(bookName=request['bookName'])
        if 'bookType' in request.keys():
            B = B.objects.filter(bookType=request['bookType'])
        if 'authors' in request.keys():
            B = B.objects.filter(authors=request['authors'])
        if 'publisher' in request.keys():
            B = B.objects.filter(publisher=request['publisher'])

        return B

    def deleteBook(self, request):
        """ delete existing book """
        R = Resource.objects.getResourceById(request)
        B = Book.objects.get(resource=R)
        B.delete()
        R.delete()
        return B


class Book(models.Model):
    TEXT_BOOK = 0
    REFERENCE_BOOK = 1
    BOOK_TYPE_CHOICES = ((TEXT_BOOK, 'Text Book'), (REFERENCE_BOOK, 'Reference Book'))

    # Resource
    resource = models.OneToOneField(Resource, on_delete=models.CASCADE, primary_key=True)
    # Book name
    bookName = models.CharField(max_length=250, blank=False, null=False)
    # Authors
    authors = models.CharField(max_length=250)
    # Edition
    edition = models.PositiveIntegerField()
    # Publisher
    publisher = models.CharField(max_length=100)
    # Book Type
    bookType = models.PositiveIntegerField(choices=BOOK_TYPE_CHOICES, null=False, blank=False)

    objects = BookManager()

    def __str__(self):
        return self.bookName + " - " + self.authors + " - " + str(self.edition) + " - " + self.publisher
