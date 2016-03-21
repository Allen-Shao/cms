from cmsapp.views import CallCenterReport
from rest_framework import serializers

class ReportSerializer(serializers.ModelSerializer):
    """
    Serializer for call center reports
    """

    class Meta:
        model = CallCenterReport
        exclude = ["status"]
