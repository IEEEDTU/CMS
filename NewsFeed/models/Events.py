from django.db import models
from Course.models import *
from Profiler.models import Mobile

#just for checking
import datetime

# Manager class for the mobile class
'''class MobileManager(models.Manager):
    def addContacts(self, request):
        """add contact numbers in the database"""
        M = Mobile(
            countryCode=request['countryCode'],
            mobileNum=request['mobileNum']
        )
        M.save()
        return M


#This class is just used to store the mobile number for the required event
class Mobile(models.Model):
    # Country Code
    countryCode = models.PositiveIntegerField(blank=False, null=False)
    # Mobile Number
    mobileNum = models.PositiveIntegerField(blank=False, null=False)

    objects = MobileManager()

    def __str__(self):
        return str(self.countryCode) + "-" + str(self.mobileNum)'''


class EventsManager(models.Manager):
    def addEvent(self, request):
        M = Mobile.objects.addContacts(request)
        E = Events(
            eventName = request['eventName'],
            startDateAndTime = request['startDateAndTime'],
            endDateAndTime = request['endDateAndTime'],
            description = request['description'],
            organisedBy = request['organisedBy'],
            personalMobile = M[0],
            alternativeMobile = M[1],
            email = request['email'],
            fbEvent = request['fbEvent'],
            website = request['website'],
            #image = ''
        )
        E.save()
        return E

    def editEvent(self,request):
        pass

    def deleteEvent(self,request):
        E = Events.objects.get(id = request['id'])
        E = E.delete()
        return E


class Events(models.Model):
    #Name of the particular event
    eventName = models.CharField(max_length=50, blank=False, null=False)
    #Start date and time of the event
    startDateAndTime = models.DateTimeField(default=False)
    #End date and time of the event
    endDateAndTime = models.DateTimeField(default=False)
    #Description of the event
    description = models.CharField(max_length=500, blank=False, null=False)
    #Organised By
    organisedBy = models.CharField(max_length=150, blank=False, null=False)
    #Contact Number
    personalMobile = models.ForeignKey(Mobile, related_name="%(class)s_personal_mobile", on_delete=models.CASCADE, default=False)
    alternativeMobile = models.ForeignKey(Mobile, related_name="%(class)s_alternative_mobile", on_delete=models.CASCADE, default=False)
    #email ID
    email = models.EmailField(blank=False, null=False, default=False)
    #Facebook Event Link
    fbEvent = models.CharField(max_length=500, blank=False, null=False)
    #Website
    website = models.CharField(max_length=75, blank=False, null=False)
    #Image
    image = models.BinaryField(null=True)

    objects = EventsManager()

    def __str__(self):
        return str(self.eventName) + "-" + str(self.startDateAndTime)


mobile0 = {
	'personalMobile':{'countryCode':91,'mobileNum':9999955533},
	'alternativeMobile':{'countryCode':91,'mobileNum':9999955533},
}
drAdd={
    'eventName':'Mid Sems 16',
    'startDateAndTime':'2016-04-04 20:04:50.308998',
    'endDateAndTime':'2016-04-04 20:04:50.308998',
    'description':'Mid Sems Starting 2016',
    'organisedBy':'DTU',
    'personalMobile':{'countryCode':91,'mobileNum':9999955533},
	'alternativeMobile':{'countryCode':91,'mobileNum':9999955533},
    'email':'example@example.com',
    'fbEvent':'www.facebook.com',
    'website':'www.dtu.ac.in',
    'image':''
}

drEdit={
    'id':'1',
    'eventName':'Mid Sems 16',
    'startDateAndTime':'2016-04-04 20:04:50.308998',
    'endDateAndTime':'2016-04-04 20:04:50.308998',
    'description':'Mid Sems Starting 2016',
    'organisedBy':'DTU',
    'personalMobile':{'countryCode':91,'mobileNum':9999955533},
	'alternativeMobile':{'countryCode':91,'mobileNum':9999955533},
    'email':'example@example.com',
    'fbEvent':'www.facebook.com',
    'website':'www.dtu.ac.in',
    'image':''
}