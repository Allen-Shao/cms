from django.shortcuts import render
# just for testing
from django.views.generic.base import TemplateView

# Create your views here.
class HomeView(TemplateView):

    template_name = "login.html"

class DashboardView(TemplateView):

    template_name = "login.html"

class NotificationView(TemplateView):

    template_name = "login.html"

class ReportView(TemplateView):

    template_name = "login.html"

class ResourceView(TemplateView):

    template_name = "login.html"

class LoginView(TemplateView):

    template_name = "login.html"
