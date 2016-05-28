from django.db import models
from .Branch import *
from .AcademicDegree import *


class CourseManager(models.Manager):
    def __generateCourseId__(self, request):
        """ generates course ID on the basis of branch, degree, semester """
        # code here...
        id = ""

        return id

    def addCourse(self, request):
        """ add new course """
        C = Course(
            courseId = request['courseId'],
            courseName = request['courseName'],
            courseType = request['courseType'],
            description = request['description'],
            credits = request['credits'],
            sessMaxMarks = request['sessMaxMarks'],
            endMaxSemMarks = request['endMaxSemMarks'],
            maxMarks = request['maxMarks'],
            minPassingMarks = request['minPassingMarks'],
            semester = request['semester'],
            degree = Degree.objects.get(degreeCode=request['degreeCode'], degreeType=request["degreeType"]),
            branch = Branch.objects.get(branchCode=request['branchCode'])
        )
        C.save()
        return C

    def editCourse(self, request):
        """ edit existing course on the basis of course ID """
        """ note: degree and branch are not editable fields """
        C = Course.objects.get(courseId=request["courseId"])
        C.courseId = request["courseId"]
        C.courseName = request["courseName"]
        C.courseType = request["courseType"]
        C.description = request["description"]
        C.credits = request["credits"]
        C.sessMaxMarks = request["sessMaxMarks"]
        C.endMaxSemMarks = request["endMaxSemMarks"]
        C.maxMarks = request["maxMarks"]
        C.minPassingMarks = request["minPassingMarks"]
        C.semester = request["semester"]
        C.save()
        return C

    def getCourseById(self, request):
        """ get the course details on the basis of course ID """
        C = Course.objects.get(courseId=request["courseId"])
        return C

    def deleteCourse(self, request):
        """ deletes any existing course on the basis of course ID """
        C = Course.objects.get(courseId=request["courseId"])
        C = C.delete()
        return C

    def getCoursesByName(self, request):
        """ get the course IDs on the basis of course name """
        C = Course.objects.filter(courseName=request["courseName"])
        # idList = []
        # for obj in C:
        #    idList.append(obj.courseId)
        return C

    def retrieveCourses(self, request):
        """ retrieve IDs of all the courses depending on the request """
        """ note: degree, branch is must """
        """ other optional attributes: semester, courseType """
        D = Degree.objects.get(degreeCode=request["degreeCode"], degreeType=request["degreeType"])
        C = Course.objects.filter(degree=D)

        B = Branch.objects.get(branchCode=request["branchCode"])
        C = C.filter(branch=B)

        if "semester" in request.keys():
            C = C.filter(semester=request["semester"])
        if "courseType" in request.keys():
            C = C.filter(courseType=request["courseType"])

        # idList = []
        # for obj in C:
        #    idList.append(obj.courseId)
        return C


    def retrieveOddCourses(self, request):
        """ retrieve IDs of all the courses depending on the request """
        """ note: degree, branch is must """
        """ other optional attributes: semester, courseType """
        D = Degree.objects.get(degreeCode=request["degreeCode"], degreeType=request["degreeType"])
        C = Course.objects.filter(degree=D)

        B = Branch.objects.get(branchCode=request["branchCode"])
        C = C.filter(branch=B)
        C = C.filter(semester__in=[1,3,5,7])
        if "courseType" in request.keys():
            C = C.filter(courseType=request["courseType"])

        # idList = []
        # for obj in C:
        #    idList.append(obj.courseId)
        C=C.order_by('semester')

        return C

    def retrieveEvenCourses(self, request):
        """ retrieve IDs of all the courses depending on the request """
        """ note: degree, branch is must """
        """ other optional attributes: semester, courseType """
        D = Degree.objects.get(degreeCode=request["degreeCode"], degreeType=request["degreeType"])
        C = Course.objects.filter(degree=D)

        B = Branch.objects.get(branchCode=request["branchCode"])
        C = C.filter(branch=B)
        C = C.filter(semester__in=[2, 4, 6, 8])
        if "courseType" in request.keys():
            C = C.filter(courseType=request["courseType"])

        # idList = []
        # for obj in C:
        #    idList.append(obj.courseId)
        C=C.order_by('semester')

        return C


class Course(models.Model):
    # Course ID
    courseId = models.CharField(max_length=10, primary_key=True, blank=False, null=False)
    # Course name
    courseName = models.CharField(max_length=100, blank=False, null=False)
    # Course type
    courseType = models.CharField(max_length=10, blank=False, null=False)
    # Course Description
    description = models.CharField(max_length=1000, blank=False, null=False)
    # Maximum credits
    credits = models.IntegerField()
    # Maximum sessional marks
    sessMaxMarks = models.DecimalField(decimal_places=1, max_digits=4)
    # Maximum end semester marks
    endMaxSemMarks = models.DecimalField(decimal_places=1, max_digits=4)
    # Maximum total marks
    maxMarks = models.DecimalField(decimal_places=1, max_digits=4)
    # Minimum passing marks
    minPassingMarks = models.DecimalField(decimal_places=1, max_digits=4)
    # Semester
    semester = models.PositiveIntegerField()
    # Degree
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE, default=False)
    # Branch
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, default=False)

    objects = CourseManager()

    def __str__(self):
        return self.courseId + " - " + self.courseName
