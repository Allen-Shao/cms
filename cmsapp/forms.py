from django import forms

from models import Notification

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
