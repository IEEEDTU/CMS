from django.db import models
from .Branch import *

class GroupManager(models.Manager):
    def addGroup(self, request):
        B = Branch.objects.getBranchByCode(request)
        G = Group(
                groupId = request['groupId'],
                semester =  request['semester'],
                startRollNo = request['startRollNo'],
                endRollNo = request['endRollNo'],
                branch = B,
                strength = request['strength']
            )
        G.save()
        return G
    
    def getGroupById(self, request):
        G = Group.objects.get(groupId = request['groupId'])
        return G
    
    def editGroup(self, request):
        G = Group.objects.get(groupId = request['groupId'])
        G.startRollNo = request['startRollNo']
        G.endRollNo = request['endRollNo']
        G.strength = request['strength']
        G.save()
        return G
    
    def deleteGroup(self, request):
        G = Group.objects.get(groupId = request['groupId'])
        G = G.delete()
        return G

class Group(models.Model):
    # Group ID
    groupId = models.CharField(max_length=20, blank=False, null=False)
    # Semester
    semester = models.IntegerField()
    # Starting roll number
    startRollNo = models.CharField(max_length=20, blank=False, null=False)
    # Ending roll number
    endRollNo = models.CharField(max_length=20, blank=False, null=False)
    # Branch
    branch = models.ForeignKey(Branch, on_delete = models.CASCADE, default=False)
    # Strength of the group
    strength = models.PositiveIntegerField()
    
    objects = GroupManager()
    
    def __str__(self):
        return self.groupId
