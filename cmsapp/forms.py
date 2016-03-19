from django import forms
from django.contrib.auth.models import User

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

		
class NotificationForm(form.ModelForm):
	"""
	Form for Notification
	"""
	class Meta:
		model = Notification
		fields = ['decision','description','agency']
		
