from django.contrib import admin
from models import CallCenterReport, Decision, Crisis, Notification, Place, Agency, UsefulPlace, ResourceRequest

# Register your models here.
admin.site.register(CallCenterReport)
admin.site.register(Decision)
admin.site.register(Crisis)
admin.site.register(Notification)
admin.site.register(Place)
admin.site.register(Agency)
admin.site.register(UsefulPlace)
admin.site.register(ResourceRequest)
