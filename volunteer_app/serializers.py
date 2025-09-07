from rest_framework import serializers
from volunteer_app.model import Organisations, Role, Volunteer, Comments, Admin
from django.conf import settings

class CommentSerializer(serializers.ModelSerializer):
	admin = serializers.SerializerMethodField()

	class Meta:
		model = Comments
		fields = ('id', 'admin', 'category', 'comment', 'created_at')

	def get_admin(self, obj):
		return obj.admin.name if obj.admin else None

class OrganisationSerializer(serializers.ModelSerializer):
	# status = serializers.SerializerMethodField()
	organisation_type_list = serializers.SerializerMethodField()
	organisation_type_numbers = serializers.SerializerMethodField()
	attachment = serializers.SerializerMethodField()
	comments = serializers.SerializerMethodField()

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

	def get_comments(self, obj):
		comments = Comments.objects.filter(category=1, parent_id=obj.id).exclude(comment=None).exclude(comment='').order_by('-created_at')
		return CommentSerializer(comments, many=True).data

# Minimal organisation serializer for nested use in Role
class MiniOrganisationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Organisations
		fields = ('id', 'title', 'organisation_branch')

class RoleSerializer(serializers.ModelSerializer):
	attachments = serializers.SerializerMethodField()
	organisation = MiniOrganisationSerializer(read_only=True)
	comments = serializers.SerializerMethodField()

	class Meta:
		model = Role
		fields = '__all__'

	def get_attachments(self, obj):
		if obj.attachments:
			return f"{settings.BACKEND_URL}{settings.MEDIA_URL}{obj.attachments}"
		return None

	def get_comments(self, obj):
		comments = Comments.objects.filter(category=3, parent_id=obj.id).exclude(comment=None).exclude(comment='').order_by('-created_at')
		return CommentSerializer(comments, many=True).data

class VolunteerSerializer(serializers.ModelSerializer):
	years_of_birth = serializers.SerializerMethodField()
	comments = serializers.SerializerMethodField()

	class Meta:
		model = Volunteer
		fields = '__all__'

	def get_years_of_birth(self, obj):
		if obj.year_of_birth:
			return int(obj.year_of_birth)

	def get_comments(self, obj):
		comments = Comments.objects.filter(category=2, parent_id=obj.id).exclude(comment=None).exclude(comment='').order_by('-created_at')
		return CommentSerializer(comments, many=True).data


class AdminSerializer(serializers.ModelSerializer):
	password = serializers.SerializerMethodField()
	
	def get_password(self, obj):
		return None
	
	class Meta:
		model = Admin
		fields = ('id', 'name', 'email', 'role', 'status', 'created_at', 'password')