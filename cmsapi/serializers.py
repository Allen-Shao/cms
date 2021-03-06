from cmsapp.models import CallCenterReport, Decision, ResourceRequest
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

class ReportPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallCenterReport
        fields = ["status"]

class DecisionSerializer(serializers.ModelSerializer):
    """
    Serializer for decisions
    """

    type_of_crisis = serializers.SlugRelatedField(
        read_only = True,
        slug_field = "type_of_crisis"
    )

    class Meta:
        model = Decision
        exclude = ["active"]

class DecisionPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Decision
        fields = ["active"]

class ResourceRequestSerializer(serializers.ModelSerializer):
    """
    Serializer for resource request
    """

    class Meta:
        model = ResourceRequest
        exclude = ["active"]

class ResourceRequestPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceRequest
        fields = ["active"]
