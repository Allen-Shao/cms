from django import forms
from django.contrib.auth.models import User
from .models import Notification, ResourceRequest

class LoginForm(forms.Form):
    """
    Form to log the user in
    """

    username = forms.CharField()
    password = forms.CharField()

# class NotificationForm(forms.Form):
# 	"""
# 	Form for Notification
# 	"""

# 	decision = forms.
# 	description = forms.Ch
# 	agency = forms.

		
class NotificationForm(forms.ModelForm):
	"""
	Form for Notification
	"""
	class Meta:
		model = Notification
		fields = ['decision','description','agency']
		
class ResourceForm(forms.ModelForm):
	"""
	Form for Resources
	"""

	crisis = forms.CharField()
	resource = forms.CharField()
	description = forms.CharField()

	class Meta:
		model = ResourceRequest
		fields = ['crisis','resource','description']