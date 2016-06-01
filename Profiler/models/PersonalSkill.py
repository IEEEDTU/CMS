from django.db import models


class SkillManager(models.Manager):
	def addSkill(self, request):
		""" add new skill """
		S = Skill(
			skillName=request['skillName']
		)
		S.save()
		return S

	def deleteSkill(self, request):
		""" deletes skill """
		S = Skill.objects.get(id=request['id'])
		S = S.delete()
		return S

	def retrieveSkills(self, request):
		""" retrieve skills """
		S = Skill.objects.all()
		return S


class Skill(models.Model):
	# Personal skill
	skillName = models.SlugField(max_length=200, blank=False, null=False)
	
	objects = SkillManager()
	
	def __str__(self):
		return self.skillName
