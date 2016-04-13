from django import forms
from django.forms.widgets import Select
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
    	def __init__(self, **kwargs):
        	super(NotificationForm,self).__init__(**kwargs)
        	self.fields['decision'].queryset = Decision.objects.filter(active=True)

	class Meta:
		model = Notification
		exclude = ["notify"]
        #widgets = {
        #    #"decision": Select(attrs={"class": "form-control"})
        #    "decision": BootstrapSelect
        #}

class ResourceForm(forms.ModelForm):
	"""
	Form for Resources
	"""
    	def __init__(self, **kwargs):
        	super(ResourceForm,self).__init__(**kwargs)
        	self.fields['crisis'].queryset = Decision.objects.filter(active=True)
        
    	class Meta:
        	model = ResourceRequest
        	exclude = ['date_time', 'active']

class CallCenterReportForm(forms.ModelForm):
    """
    Form for call center report
    """

    class Meta:
        model = CallCenterReport
        exclude = ["status", "date_time"]
        widgets = {
            "type_of_assistance": Select(attrs={"class": "form-control"})
        }

class DecisionForm(forms.ModelForm):
    """
    Form for Decision under dashboard
    """

    class Meta:
        model = Decision
        exclude = ['date_time','active']

class ProcessRequestForm(forms.Form):
    """
    Form for processing resource requests
    """

    id = forms.CharField(max_length=100)
    Agency = forms.CharField(max_length=100)
