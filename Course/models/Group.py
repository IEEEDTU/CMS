from django.db import models
from .Branch import *


class GroupManager(models.Manager):
    def __generateGroupId__(self, request):
        """ generate group id on the basis of semester and branch """
        id = 'A' if (request['semester']%2 != 0) else 'B'
        B = Branch.objects.get(branchCode=request['branchCode'])
        G = Group.objects.filter(branch=B, groupId__startswith=id).order_by('-groupId')
        if G.exists() == True:
            lastId = G[0].groupId[-1:]
            id += chr(ord(lastId) + 1)
        else:
            id += '1'
        return id

    def addGroup(self, request):
        """ add new group """
        B = Branch.objects.getBranchByCode(request)
        G = Group(
            groupId=self.__generateGroupId__(request),
            semester=request['semester'],
            startRollNo=request['startRollNo'],
            endRollNo=request['endRollNo'],
            branch=B,
            strength=request['strength']
        )
        G.save()
        return G

    def editGroup(self, request):
        """ edits an existing group """
        G = Group.objects.get(groupId=request['groupId'])
        G.startRollNo = request['startRollNo']
        G.endRollNo = request['endRollNo']
        G.strength = request['strength']
        G.save()
        return G

    def deleteGroup(self, request):
        """ delete an existing group """
        G = Group.objects.get(groupId=request['groupId'])
        G = G.delete()
        return G

    def getGroupByIdAndCode(self, request):
        """ get group on the basis of ID """
        B = Branch.objects.get(branchCode=request['branchCode'])
        G = Group.objects.get(groupId=request['groupId'], branch=B)
        return G

    def retrieveGroups(self, request):
        """ retrieve groups on the basis of branch """
        B = Branch.objects.get(branchCode=request['branchCode'])
        G = Group.objects.filter(branch=B)
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
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, default=False)
    # Strength of the group
    strength = models.PositiveIntegerField()

    objects = GroupManager()

    def __str__(self):
        return self.groupId
