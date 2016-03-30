from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
# just for testing
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.base import TemplateView, RedirectView, ContextMixin
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login, logout

from forms import LoginForm, CallCenterReportForm, NotificationForm, ResourceForm, DecisionForm

from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from models import CallCenterReport, Decision, Agency, Crisis

#SocialMedia Imports
#from Facebook import share_on_facebook
from Twitter import post_on_twitter
from Email import send_to_pres,send_to_agency
from SMS import send_sms

# Create your views here.
class CmsBaseView(ContextMixin):

    def get_context_data(self, **kwargs):
        context = super(CmsBaseView, self).get_context_data(**kwargs)
        context["is_dm"] = self.request.user.groups.filter(name='Decision Maker').exists()
        context["is_ccs"] = self.request.user.groups.filter(name='Call Center Staff').exists()
        context["is_agency"] = self.request.user.groups.filter(name='Agency Staff').exists()
        context["is_cmsstaff"] = self.request.user.groups.filter(name='CMS Staff').exists()
        context["is_staff"] = self.request.user.is_staff
        context["user_authenticated"] = self.request.user.is_authenticated()
        return context

class HomeView(CmsBaseView, TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
       context = super(HomeView, self).get_context_data(**kwargs)
       context["home_active"] = "active"
       context["user_authenticated"] = self.request.user.is_authenticated()
       context["active_decision"] = Decision.objects.filter(active = True).exists()
       print context["active_decision"]
       return context

@method_decorator(login_required, name='dispatch')
class DashboardView(CmsBaseView, SuccessMessageMixin, FormView):

    template_name = "dashboard.html"
    form_class = DecisionForm
    second_form_class = NotificationForm
    success_url="/dashboard/"
    success_message = "fail"

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context["form"] = DecisionForm
        if 'form2' not in context:
            context["form2"] = NotificationForm
        context["dashboard_active"] = "active"
        context["reports"] = CallCenterReport.objects.all()
        context["agencies"]=Agency.objects.all()
        print Agency.objects.all()
        print "agencies in context"
        return context

    def form_valid(self, form):
        form.save()
        report = CallCenterReport.objects.filter(type_of_crisis=form.cleaned_data["type_of_crisis"])
        print self.request.POST.getlist('agency')
        agencies = Agency.objects.filter(name__in= self.request.POST.getlist('agency'))
        for agency in agencies:
            print agency.contact
            print agency.name
            #Note
            #send_sms(agency.contact, "EMERGENCY!!!" + title)

        print report
        title = form.cleaned_data['type_of_crisis'].type_of_crisis
        #share_on_facebook(title, form.cleaned_data["description"])
        post_on_twitter("EMERGENCY!! " + title)
        send_to_pres("EMERGENCY!!\n\n" + title + "\n\n" + form.cleaned_data["description"])
        send_sms("EMERGENCY!! " + title)
        self.success_message = "success"
        print self.success_message
        return super(DashboardView, self).form_valid(form)



#@method_decorator(login_required, name='dispatch')
class ProcessReportsView(CmsBaseView, TemplateView):

    template_name = "process-reports.html"

    def get_context_data(self, **kwargs):
        context = super(ProcessReportsView, self).get_context_data(**kwargs)
        context["type_of_crisis"] = Crisis.objects.all()
        return context

class ProcessRequestsView(CmsBaseView, TemplateView):

    template_name = "process-requests.html"

    def get_context_data(self, **kwargs):
        context = super(ProcessRequestsView, self).get_context_data(**kwargs)
        context["agency_list"] = Agency.objects.all()
        return context

@method_decorator(login_required, name='dispatch')
class NotificationView(CmsBaseView, SuccessMessageMixin, FormView):

    template_name = "notification.html"
    form_class = NotificationForm
    success_url="/notification/"
    success_message = "fail"

    def form_valid(self, form):
        form.save()
        send_to_agency(form.cleaned_data["decision"] + "\n\n" + form.cleaned_data["description"])
        send_sms("NOTIFICATION" + form.cleaned_data["decision"])
        self.success_message = "success"
        return super(NotificationView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(NotificationView, self).get_context_data(**kwargs)
        context["form"] = NotificationForm
        context["notification_active"] = "active"
        #context["notification_view"]
        return context

@method_decorator(login_required, name='dispatch')
class ReportView(CmsBaseView, SuccessMessageMixin, FormView):

    template_name = "report.html"
    form_class = CallCenterReportForm
    success_url = "/report/"
    success_message = "fail"

    def get_context_data(self, **kwargs):
        context = super(ReportView, self).get_context_data(**kwargs)
        context["form"] = CallCenterReportForm
        context["report_active"] = "active"
        return context

    def form_valid(self, form):
        form.save()
        self.success_message = "success"
        return super(ReportView, self).form_valid(form)

class ResourceView(CmsBaseView, SuccessMessageMixin ,FormView):

    template_name = "resource.html"
    form_class = ResourceForm
    success_url = "/resource/"
    success_message = "fail"
    #NOTE: For testing, remove later
    #Make the crisis a dropdown menu
    def get_context_data(self, **kwargs):
        context = super(ResourceView, self).get_context_data(**kwargs)
        context["form"] = ResourceForm
        context["resource_active"] = "active"
        return context

    def form_valid(self, form):
        form.save()
        self.success_message = "success"
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

class AboutView(CmsBaseView, TemplateView):

    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context["about_active"] = "active"
        return context
