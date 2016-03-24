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

from django.conf.urls import url
from views import ReportViewSet, ReportDetailView, DecisionViewSet, DecisionDetailView, ResourceRequestViewSet, ResourceRequestDetailView

app_name="cmsapp"

urlpatterns = [
    url(r'^reports/$', ReportViewSet.as_view({"get": "list"}), name="reports"),
    url(r'^reports/(?P<pk>[0-9]+)/$', ReportDetailView.as_view(), name="report_detail"),
    url(r'^decisions/$', DecisionViewSet.as_view({"get": "list"}), name="decisions"),
    url(r'^decisions/(?P<pk>[0-9]+)/$', DecisionDetailView.as_view(), name="decision_detail"),
    url(r'^requests/$', ResourceRequestViewSet.as_view({"get": "list"}), name="requests"),
    url(r'^requests/(?P<pk>[0-9]+)/$', ResourceRequestDetailView.as_view(), name="request_detail")
]
