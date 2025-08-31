
from rest_framework import serializers
from volunteer_app.model import Organisations, Role
from django.conf import settings

class OrganisationSerializer(serializers.ModelSerializer):
	# status = serializers.SerializerMethodField()
	organisation_type_list = serializers.SerializerMethodField()
	organisation_type_numbers = serializers.SerializerMethodField()
	attachment = serializers.SerializerMethodField()

	class Meta:
		model = Organisations
		fields = '__all__'

	# def get_status(self, obj):
	#     return obj.status_display

	def get_organisation_type_list(self, obj):
		return obj.organisation_types

	def get_organisation_type_numbers(self, obj):
		return obj.organisation_type_list if obj.organisation_type_list else []

	def get_attachment(self, obj):
		if obj.attachment:
			# Return full URL for the attachment
			return f"{settings.BACKEND_URL}{settings.MEDIA_URL}{obj.attachment}"
		return None


# Minimal organisation serializer for nested use in Role
class MiniOrganisationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Organisations
		fields = ('id', 'title', 'organisation_branch')

class RoleSerializer(serializers.ModelSerializer):
	attachments = serializers.SerializerMethodField()
	organisation = MiniOrganisationSerializer(read_only=True)

	class Meta:
		model = Role
		fields = '__all__'

	def get_attachments(self, obj):
		if obj.attachments:
			return f"{settings.BACKEND_URL}{settings.MEDIA_URL}{obj.attachments}"
		return None