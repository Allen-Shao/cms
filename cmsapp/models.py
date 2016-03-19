from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CallCenterReport(models.Model):
    """
    Call center reports
    """

    #TYPE_OF_CRISIS_CHOICE = (
    #    ("DG", "Dengue"),
    #    ("HZ", "Haze"),
    #    ("TR", "Terrorism")
    #)

    TYPE_OF_ASSISTANCE_CHOICE = (
        ("EA", "Emergency Ambulance"),
        ("RE", "Rescue and Evacuation"),
        ("FF", "Fire-fighting")
    )

    name = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=8)
    location = models.CharField(max_length=100)
    description = models.TextField()
    type_of_crisis = models.ForeignKey("Crisis")
    type_of_assistance = models.CharField(max_length=2, choices=TYPE_OF_ASSISTANCE_CHOICE)
    status = models.NullBooleanField()
    date_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s - %s" % (self.id, self.name)

class Decision(models.Model):
    """
    Decisions made by decision makers
    """

    type_of_crisis = models.ForeignKey("Crisis")
    description = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return "%s - %s" % (self.id, self.type_of_crisis)

class Crisis(models.Model):
    """
    Crisis description
    """

    type_of_crisis = models.CharField(max_length=20, unique=True)

    def __unicode__(self):
        return self.type_of_crisis

class Notification(models.Model):
    """
    Notifications to be sent
    """

    decision = models.ForeignKey("Decision")
    description = models.TextField()
    agency = models.ForeignKey("Agency")

    def __unicode__(self):
        return "%s - %s" % (self.decision, self.agency)

class Place(models.Model):

    name = models.CharField(max_length=100, unique=True)
    contact = models.CharField(max_length=8)

class Agency(Place):
    """
    Government agency information
    """

    def __unicode__(self):
        return self.name

class UsefulPlace(Place):
    """
    Hospitals and etc.
    """

    TYPE_OF_PLACE = (
        ("H", "Hospital"),
        ("S", "Shelter")
    )

    location = models.CharField(max_length=100)
    type_of_place = models.CharField(max_length=1, choices=TYPE_OF_PLACE)

    def __unicode__(self):
        return self.name

class ResourceRequest(models.Model):
    """
    Resource requests information
    """

    crisis = models.ForeignKey("Decision")
    resource = models.CharField(max_length=50)
    description = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s - %s" % (self.crisis, self.resource)
