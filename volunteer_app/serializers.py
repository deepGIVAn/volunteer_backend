
from rest_framework import serializers
from volunteer_app.model import Organisations

class OrganisationSerializer(serializers.ModelSerializer):
    # status = serializers.SerializerMethodField()

    class Meta:
        model = Organisations
        fields = '__all__'

    # def get_status(self, obj):
    #     return obj.status_display
    organisation_type_list = serializers.SerializerMethodField()

    def get_status(self, obj):
        return obj.status_display

    def get_organisation_type_list(self, obj):
        return obj.organisation_types
