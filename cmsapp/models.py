from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CallCenterReport(models.Model):
    """
    Call center reports, related to :model: `type_of_crisis.Crisis`
    """

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

    class Meta:
        app_label = 'cmsapp'

class Decision(models.Model):
    """
    Decisions made by decision makers, related to :model: `type_of_crisis.Crisis`
    """

    type_of_crisis = models.ForeignKey("Crisis")
    description = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return "%s - %s" % (self.id, self.type_of_crisis)
    class Meta:
        app_label = 'cmsapp'

class Crisis(models.Model):
    """
    Crisis description
    """

    type_of_crisis = models.CharField(max_length=20, unique=True)

    def __unicode__(self):
        return self.type_of_crisis
    class Meta:
        app_label = 'cmsapp'

class Notification(models.Model):
    """
    Notifications to be sent, related to :model: `decision.Decision` and :model: `place.Place`
    """

    decision = models.ForeignKey("Decision")
    description = models.TextField()
    agency = models.ForeignKey("Agency", default="")

    def __unicode__(self):
        return "%s - %s" % (self.decision, self.agency)
    class Meta:
        app_label = 'cmsapp'

class Place(models.Model):
    """
    All the different places, such as PMO, Public, Agencies
    """

    name = models.CharField(max_length=100, unique=True)
    contact = models.CharField(max_length=8)

    def __unicode__(self):
        return self.name
    class Meta:
        app_label = 'cmsapp'

class Agency(Place):
    """
    Government agency information, extended from :model: `place.Place`
    """
    class Meta:
        app_label = 'cmsapp'

class UsefulPlace(Place):
    """
    Hospitals and etc., extended from :model: `place.Place`
    """

    TYPE_OF_PLACE = (
        ("H", "Hospital"),
        ("S", "Shelter")
    )

    location = models.CharField(max_length=100)
    type_of_place = models.CharField(max_length=1, choices=TYPE_OF_PLACE)
    class Meta:
        app_label = 'cmsapp'

class ResourceRequest(models.Model):
    """
    Resource requests information, related to :model: `crisis.Decision`
    """

    crisis = models.ForeignKey("Decision")
    resource = models.CharField(max_length=50)
    description = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return "%s - %s" % (self.crisis, self.resource)
    class Meta:
        app_label = 'cmsapp'