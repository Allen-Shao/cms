from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
# just for testing
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.base import TemplateView, RedirectView, ContextMixin
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login, logout

from forms import LoginForm, CallCenterReportForm, NotificationForm, ResourceForm, DecisionForm

from models import CallCenterReport

# Create your views here.
class CmsBaseView(ContextMixin):

    def get_context_data(self, **kwargs):
        context = super(CmsBaseView, self).get_context_data(**kwargs)
        context["is_dm"] = self.request.user.groups.filter(name='Decision Maker').exists()
        context["is_ccs"] = self.request.user.groups.filter(name='Call Center Staff').exists()
        context["is_agency"] = self.request.user.groups.filter(name='Agency Staff').exists()
        context["user_authenticated"] = self.request.user.is_authenticated()
        return context

class HomeView(CmsBaseView, TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
       context = super(HomeView, self).get_context_data(**kwargs)
       context["home_active"] = "active"
       context["user_authenticated"] = self.request.user.is_authenticated()
       return context


class DashboardView(CmsBaseView, FormView):

    template_name = "dashboard.html"
    form_class = DecisionForm
    success_url="/dashboard/"

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context["form"] = DecisionForm
        context["dashboard_active"] = "active"
        context["reports"] = CallCenterReport.objects.all()
        return context

    def form_valid(self, form):
        form.save()
        return super(DashboardView, self).form_valid(form)


class NotificationView(CmsBaseView, FormView):

    template_name = "Notification.html"
    form_class = NotificationForm
    success_url="/notification/"

    def form_valid(self, form):
        form.save()
        return super(NotificationView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(NotificationView, self).get_context_data(**kwargs)
        context["form"] = NotificationForm
        #context["notification_view"]
        return context


class ReportView(CmsBaseView, FormView):

    template_name = "report.html"
    form_class = CallCenterReportForm
    success_url = "/report/"

    def get_context_data(self, **kwargs):
        context = super(ReportView, self).get_context_data(**kwargs)
        context["form"] = CallCenterReportForm
        context["report_active"] = "active"
        return context

    def form_valid(self, form):
        form.save()
        return super(ReportView, self).form_valid(form)

class ResourceView(CmsBaseView, FormView):

    template_name = "resource.html"
    form_class = ResourceForm
    success_url = "/resource/"
    #NOTE: For testing, remove later
    #Make the crisis a dropdown menu
    def get_context_data(self, **kwargs):
        context = super(ResourceView, self).get_context_data(**kwargs)
        context["form"] = ResourceForm
        context["resource_active"] = "active"
        return context

    def form_valid(self, form):
        form.save()
        return super(ResourceView, self).form_valid(form)
        # NOTE: Send an SMS/Email to respective agency

class LoginView(CmsBaseView, SuccessMessageMixin, FormView):

    template_name = "login.html"
    form_class = LoginForm
    success_url = "/"
    success_message = "fail"

    def form_valid(self, form):
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                # Redirect to a success page.
                self.success_message = "success"
                print self.success_message
                return super(LoginView, self).form_valid(form)
            else:
                # Return a 'disabled account' error message
                return HttpResponse("disabled")
        else:
            context = self.get_context_data()
            context["failed"] = True
            context = RequestContext(self.request, context)
            return render_to_response(self.template_name, context)

class LogoutView(RedirectView):

    url = "/"

    def get_redirect_url(self, *args, **kwargs):
        logout(self.request)
        return super(LogoutView, self).get_redirect_url(*args, **kwargs)

class AboutView(TemplateView):

    template_name = "about.html"
    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context["about_active"] = "active"
        return context
