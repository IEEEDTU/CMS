from django.db import models


class Skill(models.Model):
    # Specialization Field
    skillName = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.skillName

