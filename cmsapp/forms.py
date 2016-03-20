from django import forms
from django.contrib.auth.models import User
from .models import Notification, ResourceRequest, CallCenterReport, Decision

class LoginForm(forms.Form):
    """
    Form to log the user in
    """

    username = forms.CharField()
    password = forms.CharField()

class NotificationForm(forms.ModelForm):
	"""
	Form for Notification
	"""
	class Meta:
		model = Notification
		fields = ['decision','description','agency']
        #widgets = {
        #    #"decision": Select(attrs={"class": "form-control"})
        #    "decision": BootstrapSelect
        #}

class ResourceForm(forms.ModelForm):
	"""
	Form for Resources
	"""

	class Meta:
		model = ResourceRequest
		exclude = ['date_time']


class CallCenterReportForm(forms.ModelForm):
    """
    Form for call center report
    """

    class Meta:
        model = CallCenterReport
        exclude = ["status", "date_time"]

class DecisionForm(forms.ModelForm):
    """
    Form for Decision under dashboard
    """

    class Meta:
        model = Decision
        exclude = ['date_time','active']
