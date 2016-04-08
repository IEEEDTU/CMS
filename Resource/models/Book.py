from django.db import models

class Book(models.Model):
	TEXT_BOOK = 0
	REFERENCE_BOOK = 1
	BOOK_TYPE_CHOICES = ( (TEXT_BOOK, 'Text Book'), (REFERENCE_BOOK, 'Reference Book') )
	
	bookId = models.CharField(max_length=20, primary_key=True, blank=False, null=False)
	name = models.CharField(max_length=50, blank=False, null=False)
	authors = models.CharField(max_length=50)
	edition = models.CharField(max_length=20)
	type = models.PositiveIntegerField(choices=BOOK_TYPE_CHOICES, null=False, blank=False)
	publisher = models.CharField(max_length=50)
	
	