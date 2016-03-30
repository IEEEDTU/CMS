from django.core import serializers
from Profiler.models.Student import *
from Course.models import Branch
from Course.models import Degree
from Profiler.views.Person import *

def addStudent(request):
    P = addPerson(request)
    S = Student(
        rollNo = request["rollNo"],
        branch = Branch.objects.get(branchCode = request["branch"]),
        degree = Degree.objects.get(degreeCode = request["degree"]),
        admissionYear = request["admissionYear"],
        graduationYear = request["graduationYear"],
        libraryId = request["libraryId"],
        password = request["password"]
    )
    S.save()
    print(S)


dic = {
    "dtuRegId" : "DTU/2K12/B08/1501",
    "name" : Name(fname="Rahul",mname="",lname="Arora",preferredName="rahularora"),
    "permanentAdd" : Address(locality="B7 Gulabi Bagh",city="Delhi",state="Delhi",country="India",pincode=110001),
    "presentAdd" : Address(locality="B8 Gulabi Bagh",city="Delhi",state="Delhi",country="India",pincode=110001),
    "guardianAdd" : Address(locality="B8 Gulabi Bagh",city="Delhi",state="Delhi",country="India",pincode=110001),
    "personalMobile" : Mobile(countryCode=91,mobileNum=9999955566),
    "alternativeMobile" : Mobile(countryCode=91,mobileNum=9999955566),
    "personalEmail" : "rahularora@gmail.com",
    "alternativeEmail" : "rahularora@gmail.com",
    "dateOfBirth" : "1994-01-01",
    "gender" : "M",
    "category" : "GEN",
    "nationality" : "Indian",
    "religion" : "Sikh",
    "dormitory" : 1,
    "fatherName" : Name(fname="Abc",mname="",lname="Arora",preferredName="abcarora"),
    "motherName" : Name(fname="Def",mname="",lname="Arora",preferredName="defarora"),
    "rollNo" : "2K12/SE/001",
    "branch" : "SE",
    "degree" : "BTech",
    "admissionYear" : 2012,
    "graduationYear" : 2016,
    "libraryId" : "111210",
    "password" : "!@#$S_"
}


"""
def editStudent(request):
    S = Student.objects.filter(rollNo = request["rollNo"])
    S.branch = Branch.objects.filter(branchName = request["branch"])
    S.degree = Degree.objects.filter(degreeName = request["degree"])
    S.admissionYear = request["admissionYear"]
    S.graduationYear = request["graduationYear"]
    S.libraryId = request["libraryId"]
    S.password = request["password"]
    P = editPerson(request)
    S.save()
    
def deleteStudent(request):
    S = Student.objects.filter(rollNo = request["rollNo"])
    deletePerson(request)
    S.delete()    

def searchStudent(request):
    

def getStudentById(request):


def getStudentsByName(request):


def getStudentsByDegree(request):


def getStudentsByBranch(request):

"""