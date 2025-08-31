from volunteer_app.model import Organisations
from volunteer_app.decorators import admin_token_required
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from volunteer_app.serializers import OrganisationSerializer
import os
import re
from datetime import datetime
from django.conf import settings

def parse_datetime(val):
	if not val or not isinstance(val, str) or not val.strip():
		return None
	try:
		# Try parsing with timezone or full ISO
		return datetime.fromisoformat(val)
	except Exception:
		try:
			# Try parsing without timezone (with seconds)
			return datetime.strptime(val, "%Y-%m-%d %H:%M:%S")
		except Exception:
			try:
				# Try parsing ISO without seconds (e.g. 2025-08-27T14:01)
				return datetime.strptime(val, "%Y-%m-%dT%H:%M")
			except Exception:
				return None

# Handle file upload with timestamp and URL-friendly filename
def handle_file_upload(uploaded_file, path):
	if not uploaded_file:
		return None
	
	# Create media/organisations directory if it doesn't exist
	upload_dir = os.path.join(settings.MEDIA_ROOT, path)
	os.makedirs(upload_dir, exist_ok=True)
	
	# Get file extension
	name, ext = os.path.splitext(uploaded_file.name)
	
	# Create URL-friendly filename with timestamp
	timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
	safe_name = re.sub(r'[^a-zA-Z0-9_-]', '_', name)
	new_filename = f"{safe_name}_{timestamp}{ext}"
	
	# Full file path
	file_path = os.path.join(upload_dir, new_filename)
	
	# Save the file
	with open(file_path, 'wb+') as destination:
		for chunk in uploaded_file.chunks():
			destination.write(chunk)
	
	# Return relative path for storing in CharField
	return f"{path}/{new_filename}"

# Convert string booleans to Python booleans for BooleanFields
def parse_bool(val):
	if isinstance(val, bool) or val is None:
		return val
	if isinstance(val, str):
		if val.lower() in ("true", "1", "yes"): return True
		if val.lower() in ("false", "0", "no"): return False
	return None


@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
@admin_token_required
def create_organisation(request):
	try:
		# Use request.data for all fields, works for both multipart and json
		org_id = request.data.get("id", None)
		
		# Process file upload
		attachment_file = request.FILES.get("attachment")
		attachment_path = handle_file_upload(attachment_file, 'organisations') if attachment_file else None

		data = {
			"title": request.data.get("title", None),
			"organisation_name": request.data.get("organisation_name", None),
			"regions_list": request.data.getlist("regions_list[]", None) if hasattr(request.data, 'getlist') else request.data.get("regions_list", []),
			"organisation_branch": request.data.get("organisation_branch", None),
			"physical_address": request.data.get("physical_address", None),
			"postal_address": request.data.get("postal_address", None),
			"contact_name": request.data.get("contact_name", None),
			"contact_phone": request.data.get("contact_phone", None),
			"contact_email": request.data.get("contact_email", None),
			"company_aim": request.data.get("company_aim", None),
			"website": request.data.get("website", None),
			"volunteer_name": request.data.get("volunteer_name", None),
			"volunteer_phone": request.data.get("volunteer_phone", None),
			"volunteer_email": request.data.get("volunteer_email", None),
			"time_role": request.data.get("time_role", None),
			"disability": request.data.get("disability", None),
			"policies": request.data.get("policies", None),
			"risk": request.data.get("risk", None),
			"charity_number": request.data.get("charity_number", None),
			"fee": request.data.get("fee", None),
			"organisation_type_list": request.data.getlist("organisation_type_list[]", None) if hasattr(request.data, 'getlist') else request.data.get("organisation_type_list", []),
			"status": request.data.get("status", None),
			"added_date": parse_datetime(request.data.get("date_added", None)),
			"deactivated_date": parse_datetime(request.data.get("date_deactivated", None)),
			"attachment": attachment_path
		}

		for bool_field in ["disability", "policies", "risk"]:
			data[bool_field] = parse_bool(data.get(bool_field))

		# Add or update logic
		if org_id:
			# Update existing
			try:
				org = Organisations.objects.get(id=org_id)
				for key, value in data.items():
					if value is not None:
						setattr(org, key, value)
				org.save()
				return Response({"message": "Organisation updated", "id": org.id}, status=200)
			except Organisations.DoesNotExist:
				return Response({"error": "Organisation not found"}, status=404)
		else:
			# Create new
			org = Organisations.objects.create(**{k: v for k, v in data.items() if v is not None})
			return Response({"message": "Organisation created", "id": org.id}, status=201)
	except Exception as e:
		# print(e)
		return Response({"error": str(e)}, status=400)

@api_view(['GET'])
@admin_token_required
def get_all_organisations(request):
	# Logic to retrieve all organisations
	organisations = Organisations.objects.all()
	serializer = OrganisationSerializer(organisations, many=True)
	return Response(serializer.data, status=200)

@api_view(['GET'])
@admin_token_required
def get_organisation(request, id):
	try:
		organisation = Organisations.objects.get(id=id)
		serializer = OrganisationSerializer(organisation)
		return Response(serializer.data, status=200)
	except Organisations.DoesNotExist:
		return Response({"error": "Organisation not found"}, status=404)

@api_view(['DELETE'])
@admin_token_required
def delete_organisation(request, id):
	try:
		organisation = Organisations.objects.get(id=id)
		organisation.deleted_at = datetime.now()
		organisation.isdeleted = True
		organisation.save()
		return Response({"message": "Organisation deleted"}, status=200)
	except Organisations.DoesNotExist:
		return Response({"error": "Organisation not found"}, status=404)


@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
@admin_token_required
def update_organisation(request, id):
	try:
		# Use request.data for all fields, works for both multipart and json
		org_id = id

		# Handle file upload with timestamp and URL-friendly filename
		def handle_file_upload(uploaded_file):
			if not uploaded_file:
				return None
			
			# Create media/organisations directory if it doesn't exist
			upload_dir = os.path.join(settings.MEDIA_ROOT, 'organisations')
			os.makedirs(upload_dir, exist_ok=True)
			
			# Get file extension
			name, ext = os.path.splitext(uploaded_file.name)
			
			# Create URL-friendly filename with timestamp
			timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
			safe_name = re.sub(r'[^a-zA-Z0-9_-]', '_', name)
			new_filename = f"{safe_name}_{timestamp}{ext}"
			
			# Full file path
			file_path = os.path.join(upload_dir, new_filename)
			
			# Save the file
			with open(file_path, 'wb+') as destination:
				for chunk in uploaded_file.chunks():
					destination.write(chunk)
			
			# Return relative path for storing in CharField
			return f"organisations/{new_filename}"

		# Process file upload
		attachment_file = request.FILES.get("attachment")
		attachment_path = handle_file_upload(attachment_file) if attachment_file else None

		data = {
			"title": request.data.get("title", None),
			"organisation_name": request.data.get("organisation_name", None),
			"regions_list": request.data.getlist("regions_list[]", None) if hasattr(request.data, 'getlist') else request.data.get("regions_list", []),
			"organisation_branch": request.data.get("organisation_branch", None),
			"physical_address": request.data.get("physical_address", None),
			"postal_address": request.data.get("postal_address", None),
			"contact_name": request.data.get("contact_name", None),
			"contact_phone": request.data.get("contact_phone", None),
			"contact_email": request.data.get("contact_email", None),
			"company_aim": request.data.get("company_aim", None),
			"website": request.data.get("website", None),
			"volunteer_name": request.data.get("volunteer_name", None),
			"volunteer_phone": request.data.get("volunteer_phone", None),
			"volunteer_email": request.data.get("volunteer_email", None),
			"time_role": request.data.get("time_role", None),
			"disability": request.data.get("disability", None),
			"policies": request.data.get("policies", None),
			"risk": request.data.get("risk", None),
			"charity_number": request.data.get("charity_number", None),
			"fee": request.data.get("fee", None),
			"organisation_type_list": request.data.getlist("organisation_type_list[]", None) if hasattr(request.data, 'getlist') else request.data.get("organisation_type_list", []),
			"status": request.data.get("status", None),
			"added_date": parse_datetime(request.data.get("date_added", None)),
			"deactivated_date": parse_datetime(request.data.get("date_deactivated", None)),
			"attachment": attachment_path
		}

		for bool_field in ["disability", "policies", "risk"]:
			data[bool_field] = parse_bool(data.get(bool_field))

		if org_id:
			# Update existing
			try:
				org = Organisations.objects.get(id=org_id)
				for key, value in data.items():
					if value is not None:
						setattr(org, key, value)
				org.save()
				return Response({"message": "Organisation updated", "id": org.id}, status=200)
			except Organisations.DoesNotExist:
				return Response({"error": "Organisation not found"}, status=404)
	except Exception as e:
		# print(e)
		return Response({"error": str(e)}, status=400)