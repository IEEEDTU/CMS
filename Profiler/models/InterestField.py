from django.db import models


class Field(models.Model):
    # Specialization Field
    fieldName = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.fieldName
