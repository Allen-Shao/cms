from django.http import HttpResponse
# just for testing
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from .models import ResourceRequest
from django.contrib.auth import authenticate, login

from forms import LoginForm, CallCenterReportForm, NotificationForm, ResourceForm

# Create your views here.
class HomeView(TemplateView):

    template_name = "base.html"

class DashboardView(TemplateView):

    template_name = "login.html"

class NotificationView(FormView):

    template_name = "Notification.html"
    form_class = NotificationForm
    success_url="/notification/"

    def form_valid(self, form):
        decision = form.cleaned_data["decision"]
        description = form.cleaned_data["description"]
        agency = form.cleaned_data["agency"]
        form.save()
        return super(NotificationView, self).form_valid(form)


class ReportView(FormView):

    template_name = "report.html"
    form_class = CallCenterReportForm
    success_url = "/report/"

    def get_context_data(self, **kwargs):
        context = super(ReportView, self).get_context_data(**kwargs)
        context["form"] = CallCenterReportForm
        return context

    def form_valid(self, form):
        form.save()
        return super(ReportView, self).form_valid(form)

class ResourceView(FormView):
    template_name = "resource.html"
    form_class = ResourceForm
    #NOTE: For testing, remove later
    #Make the crisis a dropdown menu 
    context = {'form':ResourceForm}

    def form_valid(self, form):
        crisis = form.cleaned_data["crisis"]
        resource = form.cleaned_data["resource"]
        description = form.cleaned_data["description"]
        resourceRequest = ResourceRequest(crisis=Crisis.objects.get(type_of_crisis=crisis), 
            resource = resource, description = description)
        resourceRequest.save()
        return redirect('cmsapp:home')
        # NOTE: Send an SMS/Email to respective agency

class LoginView(FormView):

    template_name = "login.html"
    form_class = LoginForm
    success_url = "/"

    def form_valid(self, form):
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                # Redirect to a success page.
                return super(LoginView, self).form_valid(form)
            else:
                # Return a 'disabled account' error message
                return HttpResponse("disabled")
        else:
            return HttpResponse("no user")
