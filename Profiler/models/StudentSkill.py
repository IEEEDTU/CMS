from django.db import models
from .Student import *
from .PersonalSkill import *


class StudentSkillManager(models.Manager):
    def addStudentSkill(self, request):
        """ adds new student personal skill """
        SS = StudentSkill(
            student=Student.objects.getStudentByRegIdOrRollNo(request),
            skill=Skill.objects.get(skillName=request['skillName'])
        )
        SS.save()
        return SS

    def deleteStudentSkill(self, request):
        """ deletes student personal skill """
        S = Student.objects.getStudentByRegIdOrRollNo(request)
        PS = Skill.objects.get(skillName=request['skillName'])
        SS = StudentSkill.objects.get(student=S, skill=PS)
        SS.delete()
        return SS

    def retrieveStudentSkill(self, request):
        """ retrieve personal skills of a student """
        S = Student.objects.getStudentByRegIdOrRollNo(request)
        SS = StudentSkill.objects.filter(student=S)
        return SS


class StudentSkill(models.Model):
    # student
    student = models.ForeignKey(Student, on_delete=models.CASCADE, default=False)
    # skill
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, default=False)

    objects = StudentSkillManager()

    def __str__(self):
        return str(self.student) + " - " + self.skill
