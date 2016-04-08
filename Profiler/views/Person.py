from django.core import serializers
from Profiler.models.Person import *
from Course.models import Branch
from Course.models import Degree

def __eq__(obj1, obj2, keys):
    """compares two objects on the basis of keys given"""
    dict1 = {k:obj1.__dict__[k] for k in keys}
    dict2 = {k:obj2.__dict__[k] for k in keys}
    return dict1==dict2

def _addNames(*args):
    """add names in the database"""
    objs = []
    for name in args:
        name.save()
        objs.append(name)
    return objs

def _addAddresses(*args):
    """add addresses in the database"""
    objs = []
    # 1st argument should be saved as it is
    args[0].save()
    objs.append(args[0])
    
    # keys to be used for comparison
    keys = ["locality", "city", "state", "country", "pincode"]
    
    # checking 2nd argument
    # if it is same as 1st then just append 1st argument in the object list 
    # else save new item and append that in the object list
    if(__eq__(args[0],args[1],keys)):
        objs.append(args[0])
    else:
        args[1].save()
        objs.append(args[1])

    # checking 3rd argument
    # if it is same as 1st or 2nd then just append respective argument in the object list 
    # else save new item and append that in the object list
    if(__eq__(args[0],args[2],keys)):
        objs.append(args[0])
    elif(__eq__(args[1],args[2],keys)):
        objs.append(args[1])
    else:
        args[2].save()
        objs.append(args[2])    
    
    return objs

def _addContacts(*args):
    """add contact numbers in the database"""
    objs = []
    for contact in args:
        contact.save()
        objs.append(contact)
    return objs

def addPerson(request):
    """inserts person details in the database"""
    nameObjs = _addNames(request["name"], request["fatherName"], request["motherName"])
    addressObjs = _addAddresses(request["permanentAdd"], request["presentAdd"], request["guardianAdd"])
    contactObjs = _addContacts(request["personalMobile"], request["alternativeMobile"])
    
    P = Person(
        dtuRegId = request["dtuRegId"],
        name = nameObjs[0],
        permanentAdd = addressObjs[0],
        presentAdd = addressObjs[1],
        guardianAdd = addressObjs[2],
        personalMobile = contactObjs[0],
        alternativeMobile = contactObjs[1],
        personalEmail = request["personalEmail"],
        alternativeEmail = request["alternativeEmail"],
        dateOfBirth = request["dateOfBirth"],
        gender = request["gender"],
        category = request["category"],
        nationality = request["nationality"],
        religion = request["religion"],
        dormitory = request["dormitory"],
        fatherName = nameObjs[1],
        motherName = nameObjs[2]
    )
    P.save()
    return P