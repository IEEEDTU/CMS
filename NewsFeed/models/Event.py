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

    def deleteEvent(self, request):
        """ deletes an existing event """
        E = Event.objects.get(id=request['id'])
        E = E.delete()
        return E


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


event0 = {
    'eventName': 'Data Mining Workshop',
    'startDateTime': '2016-04-04 20:04:50.308998',
    'description': 'Data Mining Workshop by Vaibhav Sawhney',
    'organisedBy': 'IEEEDTU',
    'mobile': {'countryCode': 21, 'mobileNum': 9999955533},
    'email': 'example@example.com',
}
event1 = {
    'eventName': 'Data Mining Workshop',
    'startDateTime': '2016-04-05 20:04:50.308998',
    'endDateTime': '2016-04-04 20:04:50.308998',
    'description': 'Data Mining Workshop by Vaibhav Sawhney',
    'organisedBy': 'IEEEDTU',
    'mobile': {'countryCode': 21, 'mobileNum': 9999955533},
    'email': 'example@example.com',
    'fbEvent': 'www.facebook.com',
    'website': 'www.ieee.dcetech.com',
    'image': 'drive.google.co.in/image1'
}
