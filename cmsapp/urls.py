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
from views import HomeView, DashboardView, NotificationView, LoginView, ReportView, ResourceView

urlpatterns = [
    url(r'^$', HomeView.as_view()),
    url(r'^dashboard/$', DashboardView.as_view()),
    url(r'^report/$', ReportView.as_view()),
    url(r'^notification/$', NotificationView.as_view()),
    url(r'^login/$', LoginView.as_view()),
    url(r'^resource/$', ResourceView.as_view())
]
