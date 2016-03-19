from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CallCenterReport(models.Model):
    """
    Call center reports
    """

    TYPE_OF_CRISIS_CHOICE = (
        ("DG", "Dengue"),
        ("HZ", "Haze"),
        ("TR", "Terrorism")
    )
    TYPE_OF_ASSISTANCE_CHOICE = (
        ("EA", "Emergency Ambulance"),
        ("RE", "Rescue and Evacuation"),
        ("FF", "Fire-fighting")
    )

    name = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=8)
    location = models.CharField(max_length=100)
    description = models.TextField()
    type_of_crisis = models.CharField(max_length=2, choices=TYPE_OF_CRISIS_CHOICE)
    type_of_assistance = models.CharField(max_length=2, choices=TYPE_OF_ASSISTANCE_CHOICE)
    status = models.NullBooleanField()
    date_time = models.DateTimeField(auto_now_add=True)

class Decision(models.Model):
    """
    Decisions made by decision makers
    """

    description = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)

class Notification(models.Model):
    """
    Notifications to be sent
    """

    pass

class Agency(models.Model):
    """
    Government agency information
    """

    pass
