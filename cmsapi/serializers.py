from cmsapp.views import CallCenterReport
from rest_framework import serializers

class ReportSerializer(serializers.ModelSerializer):
    """
    Serializer for call center reports
    """

    # set custom display method
    type_of_assistance = serializers.SerializerMethodField()
    type_of_crisis = serializers.SlugRelatedField(
        read_only = True,
        slug_field = "type_of_crisis"
    )

    class Meta:
        model = CallCenterReport
        exclude = ["status"]

    def get_type_of_assistance(self, report):
        return report.get_type_of_assistance_display()
