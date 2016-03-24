from rest_framework import viewsets
from rest_framework.generics import UpdateAPIView
from serializers import ReportSerializer, DecisionSerializer, ReportPostSerializer
from cmsapp.models import CallCenterReport

# Create your views here.
class ReportViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing all the reports
    """

    serializer_class = ReportSerializer
    queryset = CallCenterReport.objects.filter(status__isnull = True)

class ReportDetailView(UpdateAPIView):
    """
    A view for updating reports
    """

    serializer_class = ReportPostSerializer

    def get_queryset(self):
        return CallCenterReport.objects.all()
        #return CallCenterReport.objects.get(id=self.request.id)

    def partial_update(self, request, *args, **kwargs):
        """This method is for changing the status of a specific report"""

        return super(ReportDetailView, self).update(request, *args, **kwargs)
