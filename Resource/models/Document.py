from django.db import models

class Document(models.Model):
	WORD_DOCUMENT = 0
	TEXT_FILE = 1
	PRESENTATION = 2
	PDF = 3
	DOCUMENT_TYPE_CHOICES = ( (WORD_DOCUMENT, 'Word Document'), (TEXT_FILE, 'Text File'), (PRESENTATION, 'Presentation'), (PDF, 'PDF') )
	
	documentId = models.CharField(max_length=20, primary_key=True, blank=False, null=False)
	type = models.PositiveIntegerField(choices = DOCUMENT_TYPE_CHOICES, blank=False, null=False)
	source = models.FileField(upload_to = 'Document')
	
	