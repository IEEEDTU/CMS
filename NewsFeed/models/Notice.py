from django.db import models
from Course.models import Degree, Branch, Department


class NoticeManager(models.Manager):
    def addNotice(self, request):
        """ adds new notice """
        """ note: filelink, degree, branch, department are optional """
        N = Notice(
            subject=request['subject'],
            issuingAuthority=request['issuingAuthority'],
            fileLink=request['fileLink'],
        )

        if "degreeCode" and "degreeType" in request.keys():
            N.degree = Degree.objects.getDegreeByCodeAndType(request)
        if "branchCode" in request.keys():
            N.branch = Branch.objects.getBranchByCode(request)
        if "deptId" in request.keys():
            N.department = Department.objects.getDepartmentById(request)

        N.save()
        return N

    def getNoticeById(self, request):
        """ get notice details based on notice id """
        N = Notice.objects.get(id=request['id'])
        return N

    def retrieveNotices(self, request):
        """ retrieve all the notices """
        """ optional fields: subject, issuingAuthority, degree, branch, department """
        N = Notice.objects.all()
        if 'subject' in request.keys():
            N = N.filter(subject=request['subject'])
        if 'issuingAuthority' in request.keys():
            N = N.filter(issuingAuthority=request['issuingAuthority'])
        if 'degree' in request.keys():
            N = N.filter(degree=request['degree'])
        if 'branch' in request.keys():
            N = N.filter(branch=request['branch'])
        if 'department' in request.keys():
            N = N.filter(department=request['department'])

        return N

    def deleteNotice(self, request):
        """ deletes an existing notice """
        N = Notice.objects.get(id=request['id'])
        N = N.delete()
        return N

    def retrieveLatestNotice(self, request):
        """ retrieves latest Notice """
        """ criteria is to just return top 10 news """
        lastTen = Notice.objects.filter(date>=request['since']).order_by('-date')[:10]
        return lastTen

    def retrieveMoreNotice(self, request):
        N = Notice.objects.all()
        paginator = Paginator(N, request['rowsPerPage'])
    
        page = request['page']
        try:
            notice = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            notice = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            notice = paginator.page(paginator.num_pages)
    
        return notice


class Notice(models.Model):
    # Subject
    subject = models.CharField(max_length=250, blank=False, null=False)
    # IssuingAuthority
    issuingAuthority = models.CharField(max_length=250, blank=False, null=False)
    # Issue date
    issueDate = models.DateTimeField(auto_now=False, auto_now_add=True)
    # Link of the file from DropBox
    fileLink = models.URLField(null=False, blank=False, default=False)
    # degree
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE, null=True, blank=True)
    # branch
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True, blank=True)
    # department
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)

    objects = NoticeManager()

    def __str__(self):
        return self.subject
