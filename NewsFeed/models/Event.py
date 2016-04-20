from django.db import models
from Course.models import *
from Profiler.models import Mobile
from datetime import datetime

class EventManager(models.Manager):
    def addEvent(self, request):
        """ adds new event """
        M = Mobile(
            countryCode=request["mobile"]["countryCode"],
            mobileNum=request["mobile"]["mobileNum"])
        M.save()

        E = Event(
            eventName=request['eventName'],
            startDateTime=request['startDateTime'],
            description=request['description'],
            organisedBy=request['organisedBy'],
            mobile=M,
            email=request['email'],
        )

        if "endDateTime" in request.keys():
            E.endDateTime=request['endDateTime']
        if "fbEvent" in request.keys():
            E.fbEvent=request['fbEvent']
        if "website" in request.keys():
            E.website=request['website']
        if "image" in request.keys():
            E.image=request['image']

        E.save()
        return E

    def editEvent(self, request):
        """ edit the event details """
        E = Event.objects.get(id=request['id'])
        E.eventName = request['eventName']
        E.startDateTime = request['startDateTime']
        E.endDateTime = request['endDateTime']
        E.description = request['description']
        E.organisedBy = request['organisedBy']
        M = E.mobile
        M.countryCode=request["mobile"]["countryCode"]
        M.mobileNum=request["mobile"]["mobileNum"]
        M.save()
        E.mobile = M

        if "endDateTime" in request.keys():
            E.endDateTime=request['endDateTime']
        if "fbEvent" in request.keys():
            E.fbEvent=request['fbEvent']
        if "website" in request.keys():
            E.website=request['website']
        if "image" in request.keys():
            E.image=request['image']

        E.save()
        return E

    def getEventById(self, request):
        """ get event details based on event id """
        E = Event.objects.get(id=request['id'])
        return E

    def retrieveEvents(self, request):
        """ retrieve all the events """
        """ optional fields: eventName, startDateTime, endDateTime, organisedBy """
        E = Event.objects.all()
        if 'eventName' in request.keys():
            E = E.filter(eventName=request['eventName'])
        if 'startDateTime' in request.keys():
            E = E.filter(startDateTime=request['startDateTime'])
        if 'endDateTime' in request.keys():
            E = E.filter(endDateTime=request['endDateTime'])
        if 'organisedBy' in request.keys():
            E = E.filter(organisedBy=request['organisedBy'])

        return E

    def deleteEvent(self, request):
        """ deletes an existing event """
        E = Event.objects.get(id=request['id'])
        E = E.delete()
        return E

    def retrieveLatestEvent(self, request):
        """ retrieves latest Event """
        """ criteria is to just return top 10 news """
        lastTen = Event.objects.filter(date>=request['since']).order_by('-date')[:10]
        return lastTen

    def retrieveMoreEvent(self, request):
        E = Event.objects.all()
        paginator = Paginator(E, request['rowsPerPage'])
    
        page = request['page']
        try:
            event = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            event = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            event = paginator.page(paginator.num_pages)
    
        return event


class Event(models.Model):
    # Name of the particular event
    eventName = models.CharField(max_length=250, blank=False, null=False)
    # Start date and time of the event
    startDateTime = models.DateTimeField(blank=False, null=False, default=False)
    # End date and time of the event
    endDateTime = models.DateTimeField(blank=True, null=True)
    # Description of the event
    description = models.CharField(max_length=4000, blank=False, null=False)
    # Organised By
    organisedBy = models.CharField(max_length=250, blank=False, null=False)
    # Contact Number
    mobile = models.ForeignKey(Mobile, related_name="%(class)s_mobile", on_delete=models.CASCADE, default=False)
    # email ID
    email = models.EmailField(blank=False, null=False, default=False)
    # Facebook Event Link
    fbEvent = models.URLField(blank=True, null=True)
    # Website
    website = models.URLField(blank=True, null=True)
    # Image
    image = models.URLField(blank=True, null=True)

    objects = EventManager()

    def __str__(self):
        return self.eventName + "-"
