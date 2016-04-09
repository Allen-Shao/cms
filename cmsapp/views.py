from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
# just for testing
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.base import TemplateView, RedirectView, ContextMixin
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login, logout

from forms import LoginForm, CallCenterReportForm, NotificationForm, ResourceForm, DecisionForm, ProcessRequestForm

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from models import CallCenterReport, Decision, Agency, Crisis, Notification, ResourceRequest

#SocialMedia Imports
#from Facebook import share_on_facebook
from Twitter import post_on_twitter
from Email import send_to_president
from SMS import send_sms
from Facebook import share_on_facebook

# Create your views here.
class CmsBaseView(ContextMixin):
    """
    Authenticates the user
    """

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
    """
    Displays all the active crisis on the home page.

    **Context**
    ``active_decision``
    An instance of :model:`active_decision.Decision`.

    **Template:**
    :template:`templates/home.html`

    """

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context["home_active"] = "active"
        context["user_authenticated"] = self.request.user.is_authenticated()
        context["active_decision"] = Decision.objects.filter(active = True).exists()
        return context

@method_decorator(login_required, name='dispatch')
class DashboardView(CmsBaseView, SuccessMessageMixin, FormView):
    """
    Display the general dashboard. Consists of all the active notifications and enable the decision maker to declare a crisis.

    **Context**
    ``reports``
    An instance of :model:`reports.CallCenterReport`.

    **Context**
    ``agencies``
    An instance of :model:`agencies.Agency`.

    **Template:**
    :template:`templates/dashboard.html`

    """

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
        #print "agencies in context"
        return context

    def form_valid(self, form):
        form.save()
        #report = CallCenterReport.objects.filter(type_of_crisis=form.cleaned_data["type_of_crisis"])
        title = form.cleaned_data['type_of_crisis'].type_of_crisis

        agencies = Agency.objects.filter(name__in= self.request.POST.getlist('agency'))
        for agency in agencies:
            print agency.contact
            print agency.name
            send_sms(agency.contact, "EMERGENCY!! " + title)

        share_on_facebook(title, form.cleaned_data["description"])
        post_on_twitter("EMERGENCY!! " + title)
        send_to_president("EMERGENCY!!\n\n" + title + "\n\n" + form.cleaned_data["description"])
        #send_sms("86897793","EMERGENCY!! " + title)

        self.success_message = "success_submission"
        print self.success_message
        return super(DashboardView, self).form_valid(form)



@method_decorator(login_required, name='dispatch')
class ProcessReportsView(CmsBaseView, TemplateView):
    """
    Display an individual :model:`report.CallCenterReport`. Processing the reports from the call center staff

    **Context**
    ``report``
    An instance of :model:`report.CallCenterReport`.

    **Context**
    ``type_of_crisis``
    An instance of :model:`type_of_crisis.Crisis`

    **Template:**
    :template:`templates/process-reports.html`

    """

    template_name = "process-reports.html"

    def get_context_data(self, **kwargs):
        context = super(ProcessReportsView, self).get_context_data(**kwargs)
        context["process_report_active"] = "active"
        context["type_of_crisis"] = Crisis.objects.all()
        return context

@method_decorator(login_required, name='dispatch')
class ProcessRequestsView(CmsBaseView, FormView):
    """
    Display an individual :model:`resourceRequest.ResourceRequest`. Processing the requests made by agencies

    **Context**
    ``agency_list``
    An instance of :model:`agency_list.Agency`.

    **Context**
    ``resourceRequest``
    An instance of :model:`resourceRequest.ResourceRequest`.

    **Template:**
    :template:`templates/process-requests.html`

    """

    template_name = "process-requests.html"
    form_class = ProcessRequestForm
    success_url = "/login/"

    def get_context_data(self, **kwargs):
        context = super(ProcessRequestsView, self).get_context_data(**kwargs)
        context["process_request_active"] = "active"
        context["agency_list"] = Agency.objects.all()
        return context

    def form_valid(self, form):
        request_id = form.cleaned_data["id"]
        request = ResourceRequest.objects.get(pk=request_id)
        agency_name = form.cleaned_data["Agency"]
        agency = Agency.objects.get(name=agency_name)
        request.active = False
        #send_sms(agency.contact,"RESOURCE REQUEST: \nType Of Crisis: " + request.crisis.type_of_crisis + \
        #        "\nResource Requested: " + request.resource + "\nDescription: " + request.description)
        request.save()

        return super(ProcessRequestsView, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class NotificationView(CmsBaseView, SuccessMessageMixin, FormView):
    """
    Display an individual :model:`notification.Notification`. Sending notifications to the required parties.

    **Context**
    ``notification``
    An instance of :model:`notification.Notification`.

    **Context**
    ``place``
    An instance of :model: `place.Places`

    **Template:**
    :template:`templates/notification.html`

    """

    template_name = "notification.html"
    form_class = NotificationForm
    success_url="/notification/"
    success_message = "fail"

    def form_valid(self, form):
        #form.save()
        print self.request.POST.get("facebook")
        print self.request.POST.get("twitter")
        print self.request.POST.get("pmo")
        print self.request.POST.get("agency_check")
        print form.cleaned_data["decision"]
        decision = Decision.objects.all().get(id=self.request.POST.get("decision"))
        title = decision.type_of_crisis.type_of_crisis
        notify = ""
        #Push Notifications
        if self.request.POST.get("facebook") == "facebook":
            #share_on_facebook(title, form.cleaned_data["description"])
            notify += "Facebook,"
        if self.request.POST.get("twitter") == "twitter":
            post_on_twitter(title + " " +form.cleaned_data["description"])
            notify += "Twitter,"
        if self.request.POST.get("pmo") == "pmo":
            send_to_president("NOTIFICATION!!\n\n" + title + "\n\n" + str(form.cleaned_data["description"]))
            notify += "Email,"

        agencies = Agency.objects.filter(name__in= self.request.POST.getlist('agency'))
        if agencies != None:
            for agency in agencies:
                notify += agency.name + ","
                #send_sms(agency.contact,"NOTIFICATION " + str(form.cleaned_data["decision"])[4:])


        #Saving the notification to the database.
        notif = Notification(
                    notify = notify,
                    decision=form.cleaned_data["decision"],
                    description=form.cleaned_data["description"]
                    )
        notif.save()

        print str(form.cleaned_data["decision"])[4:] + "\n\n" + form.cleaned_data["description"]
        self.success_message = "success_submission"

        return super(NotificationView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(NotificationView, self).get_context_data(**kwargs)
        context["form"] = NotificationForm
        context["agencies"] = Agency.objects.all()
        context["notification_active"] = "active"
        #context["notification_view"]
        return context

@method_decorator(login_required, name='dispatch')
class ReportView(CmsBaseView, SuccessMessageMixin, FormView):
    """
    Display an individual :model:`report.CallCenterReport`. Allowing the call center staffs to make reports

    **Context**
    ``report``
    An instance of :model:`report.CallCenterReport`.

    **Template:**
    :template:`templates/report.html`

    """

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
        self.success_message = "success_submission"
        return super(ReportView, self).form_valid(form)

@method_decorator(login_required, name='dispatch')
class ResourceView(CmsBaseView, SuccessMessageMixin ,FormView):
    """
    To request resources upon reaching the required position. Used by the agency staffs

    **Context**
    ``resourceRequest``
    An instance of :model:`resourceRequest.ResourceRequest`.

    **Template:**
    :template:`templates/resource.html`

    """

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
        self.success_message = "success_submission"
        return super(ResourceView, self).form_valid(form)
        # NOTE: Send an SMS/Email to respective agency

class LoginView(CmsBaseView, SuccessMessageMixin, FormView):
    """
    Logs the user in the system. The user can be either the decision maker, a CMS staff, a call center staff, an agency staff or the django admin.

    **Template:**
    :template:`templates/login.html`

    """

    template_name = "login.html"
    form_class = LoginForm
    success_url = "/"
    success_message = "fail"

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        next_url = self.request.GET.get("next", None)
        if next_url is not None:
            context["next"] = self.request.GET["next"]
        return context

    def form_valid(self, form):
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                # Redirect to a success page.
                self.success_message = "success"
                # decide which page to jump to
                next_url = self.request.POST.get("next", None)
                if next_url is not None:
                    self.success_url = next_url
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
    """
    Logs the user out of the system
    """

    url = "/"

    def get_redirect_url(self, *args, **kwargs):
        logout(self.request)
        return super(LogoutView, self).get_redirect_url(*args, **kwargs)

class AboutView(CmsBaseView, TemplateView):
    """
    Information about the Crisis Management System

    **Template:**
    :template:`templates/about.html`

    """

    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context["about_active"] = "active"
        return context
