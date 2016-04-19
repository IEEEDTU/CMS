from django.contrib import admin
from .models import Resource, Book, Publication, Document, WebLink

admin.site.register(Resource)
admin.site.register(Book)
admin.site.register(Publication)
admin.site.register(Document)
admin.site.register(WebLink)
