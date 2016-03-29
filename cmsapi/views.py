from rest_framework import viewsets
from rest_framework.generics import UpdateAPIView
from serializers import ReportSerializer, DecisionSerializer, ReportPostSerializer, DecisionPostSerializer, ResourceRequestSerializer, ResourceRequestPostSerializer
from cmsapp.models import CallCenterReport, Decision, ResourceRequest

# Create your views here.
class ReportViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing all the reports
    """

    serializer_class = ReportSerializer

    def get_queryset(self):
        queryset = CallCenterReport.objects.filter(status__isnull = True)
        type_of_crisis = self.request.query_params.get("type", None)
        if type_of_crisis is not None:
            queryset = queryset.filter(type_of_crisis__type_of_crisis=type_of_crisis)
        return queryset


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

class DecisionViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing all active crisis
    """

    serializer_class = DecisionSerializer
    queryset = Decision.objects.filter(active = True)

class DecisionDetailView(UpdateAPIView):
    """
    A view for updating crisis status
    """

    serializer_class = DecisionPostSerializer

    def get_queryset(self):
        return Decision.objects.all()

    def partial_update(self, request, *args, **kwargs):
        """This method is for changing the status of a specific crisis"""

        return super(DecisionDetailView, self).update(request, *args, **kwargs)

class ResourceRequestViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing all active resource requests
    """

    serializer_class = ResourceRequestSerializer
    queryset = ResourceRequest.objects.filter(active = True)

class ResourceRequestDetailView(UpdateAPIView):
    """
    A view for updating resource request status
    """

    serializer_class = ResourceRequestPostSerializer

    def get_queryset(self):
        return ResourceRequest.objects.all()

    def partial_update(self, request, *args, **kwargs):
        """This method is for changing the status of a specific resource request"""

        return super(ResourceRequestDetailView, self).update(request, *args, **kwargs)
