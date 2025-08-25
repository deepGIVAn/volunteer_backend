
from rest_framework import serializers
from volunteer_app.model import Organisations
from django.conf import settings

class OrganisationSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    organisation_type_list = serializers.SerializerMethodField()
    attachment = serializers.SerializerMethodField()

    class Meta:
        model = Organisations
        fields = '__all__'

    def get_status(self, obj):
        return obj.status_display

    def get_organisation_type_list(self, obj):
        return obj.organisation_types

    def get_attachment(self, obj):
        if obj.attachment:
            # Return full URL for the attachment
            return f"{settings.BACKEND_URL}{settings.MEDIA_URL}{obj.attachment}"
        return None
