"""cms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from views import HomeView, DashboardView, NotificationView, ProcessReportsView, ProcessRequestsView, LoginView, ReportView, ResourceView, LogoutView, AboutView

app_name="cmsapp"

urlpatterns = [
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^dashboard/$', DashboardView.as_view(), name="dashboard"),
    url(r'^report/$', ReportView.as_view(), name="report"),
    url(r'^process-reports/$', ProcessReportsView.as_view(), name="process-reports"),
    url(r'^process-requests/$', ProcessRequestsView.as_view(), name="process-requests"),
    url(r'^notification/$', NotificationView.as_view(), name="notification"),
    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^resource/$', ResourceView.as_view(), name="resource"),
    url(r'^logout/$', LogoutView.as_view(), name="logout"),
    url(r'^about/$',AboutView.as_view(), name="about")
]
