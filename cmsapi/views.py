from rest_framework import viewsets
from serializers import ReportSerializer
from cmsapp.models import CallCenterReport

# Create your views here.
class ReportViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing all the reports
    """

    serializer_class = ReportSerializer
    queryset = CallCenterReport.objects.filter(status__isnull = True)
