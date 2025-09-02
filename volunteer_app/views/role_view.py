from volunteer_app.decorators import admin_token_required
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
import os
import re
from datetime import datetime
from django.conf import settings
from .organisation_view import parse_datetime, handle_file_upload, parse_bool, add_comment
from volunteer_app.model import Role
import random
from volunteer_app.serializers import RoleSerializer

def generate_4_digit_number_str():
	return f"{random.randint(0, 9999):04d}"

@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
@admin_token_required
def create_role(request):
	try:
		attachment_file = request.FILES.get("attachments")
		attachment_path = handle_file_upload(attachment_file, 'roles') if attachment_file else None

		data = {
			"roleId": f"{generate_4_digit_number_str()}",
			"title": request.data.get("title", None),
			"organisation_id": request.data.get("organisation", None),
			"contact": request.data.get("contact", None),
			"branch": request.data.get("branch", None),
			"status": request.data.get("status", None),
			"vols_req": request.data.get("vols_req", None),
			"reports": request.data.get("reports", None),
			"email": request.data.get("email", None),
			"date_added": parse_datetime(request.data.get("date_added", None)),
			"description": request.data.get("description", None),
			"results": request.data.get("results", None),
			"leagues_hours": request.data.get("leagues_hours", None),
			"skills": request.data.get("skills", None),
			"personality": request.data.get("personality", None),
			"criminal": request.data.get("criminal", None),
			"transport": request.data.get("transport", None),
			"wheelchair": request.data.get("wheelchair", None),
			"toilet": request.data.get("toilet", None),
			"stairs": request.data.get("stairs", None),
			"home": request.data.get("home", None),
			"oneoff": request.data.get("oneoff", None),
			"leagues_days": request.data.get("leagues_days", None),
			"start_date": parse_datetime(request.data.get("start_date", None)),
			"end_date": parse_datetime(request.data.get("end_date", None)),
			"training": request.data.get("training", None),
			"reimbursement": request.data.get("reimbursement", None),
			"reimbursement_other": request.data.get("reimbursement_other", None),
			"supervision": request.data.get("supervision", None),
			"other": request.data.get("other", None),
			"paid_job": request.data.get("paid_job", None),
			"notes": request.data.get("notes", None),
			"filter_color": request.data.get("filter_color", None),
			"youth": request.data.get("youth", None),
			"english": request.data.get("english", None),
			"disability": request.data.get("disability", None),
			"mental": request.data.get("mental", None),
			"region_of_placement_list": request.data.getlist("region_of_placement_list[]", None) if hasattr(request.data, 'getlist') else request.data.get("region_of_placement_list", []),
			"days_list": request.data.getlist("days_list[]", None) if hasattr(request.data, 'getlist') else request.data.get("days_list", []),
			"time_list": request.data.getlist("time_list[]", None) if hasattr(request.data, 'getlist') else request.data.get("time_list", []),
			"activities_driving_list": request.data.getlist("activities_driving_list[]", None) if hasattr(request.data, 'getlist') else request.data.get("activities_driving_list", []),
			"activities_administration_list": request.data.getlist("activities_administration_list[]", None) if hasattr(request.data, 'getlist') else request.data.get("activities_administration_list", []),
			"activities_mantinance_list": request.data.getlist("activities_mantinance_list[]", None) if hasattr(request.data, 'getlist') else request.data.get("activities_mantinance_list", []),
			"activities_home_cares_list": request.data.getlist("activities_home_cares_list[]", None) if hasattr(request.data, 'getlist') else request.data.get("activities_home_cares_list", []),
			"activities_technology_list": request.data.getlist("activities_technology_list[]", None) if hasattr(request.data, 'getlist') else request.data.get("activities_technology_list", []),
			"activities_event_list": request.data.getlist("activities_event_list[]", None) if hasattr(request.data, 'getlist') else request.data.get("activities_event_list", []),
			"activities_hospitality_list": request.data.getlist("activities_hospitality_list[]", None) if hasattr(request.data, 'getlist') else request.data.get("activities_hospitality_list", []),
			"activities_support_list": request.data.getlist("activities_support_list[]", None) if hasattr(request.data, 'getlist') else request.data.get("activities_support_list", []),
			"activities_financial_list": request.data.getlist("activities_financial_list[]", None) if hasattr(request.data, 'getlist') else request.data.get("activities_financial_list", []),
			"activities_other_list": request.data.getlist("activities_other_list[]", None) if hasattr(request.data, 'getlist') else request.data.get("activities_other_list", []),
			"activities_sport_list": request.data.getlist("activities_sport_list[]", None) if hasattr(request.data, 'getlist') else request.data.get("activities_sport_list", []),
			"activities_group_list": request.data.getlist("activities_group_list[]", None) if hasattr(request.data, 'getlist') else request.data.get("activities_group_list", []),
			"attachments": attachment_path,
		}
		
		for bool_field in ["criminal", "transport", "wheelchair", "toilet", "stairs", "home", "oneoff", "paid_job", "youth", "english", "disability", "mental"]:
			data[bool_field] = parse_bool(data.get(bool_field))
		
		role = Role.objects.create(**{k: v for k, v in data.items() if v is not None})
		add_comment(3, role.id, request.data.get("comment", None), request.admin) # 3 for Role
		return Response({"message": "Role created successfully", "id": role.id}, status=201)
	except Exception as e:
		# print(e)
		return Response({"error": str(e)}, status=400)

@api_view(['GET'])
@admin_token_required
def get_all_roles(request):
	try:
		roles = Role.objects.all()
		serializer = RoleSerializer(roles, many=True)
		return Response(serializer.data)
	except Exception as e:
		return Response([], status=400)

@api_view(['GET'])
@admin_token_required
def get_role(request, id):
	try:
		role = Role.objects.get(id=id)
		serializer = RoleSerializer(role)
		return Response(serializer.data, status=200)
	except Role.DoesNotExist:
		return Response({"error": "Role not found"}, status=404)
	except Exception as e:
		return Response({"error": str(e)}, status=400)

@api_view(['DELETE'])
@admin_token_required
def delete_role(request, id):
	try:
		role = Role.objects.get(id=id)
		role.deleted_at = datetime.now()
		role.isdeleted = True
		role.save()
		return Response({"message": "Role deleted"}, status=200)
	except Role.DoesNotExist:
		return Response({"error": "Role not found"}, status=404)

@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
@admin_token_required
def update_role(request, id):
	try:
		attachment_file = request.FILES.get("attachments")
		attachment_path = handle_file_upload(attachment_file, 'roles') if attachment_file else None

		data = {
			"title": request.data.get("title", None),
			"organisation_id": request.data.get("organisation", None),
			"contact": request.data.get("contact", None),
			"branch": request.data.get("branch", None),
			"status": request.data.get("status", None),
			"vols_req": request.data.get("vols_req", None),
			"reports": request.data.get("reports", None),
			"email": request.data.get("email", None),
			"date_added": parse_datetime(request.data.get("date_added", None)),
			"description": request.data.get("description", None),
			"results": request.data.get("results", None),
			"leagues_hours": request.data.get("leagues_hours", None),
			"skills": request.data.get("skills", None),
			"personality": request.data.get("personality", None),
			"criminal": request.data.get("criminal", None),
			"transport": request.data.get("transport", None),
			"wheelchair": request.data.get("wheelchair", None),
			"toilet": request.data.get("toilet", None),
			"stairs": request.data.get("stairs", None),
			"home": request.data.get("home", None),
			"oneoff": request.data.get("oneoff", None),
			"leagues_days": request.data.get("leagues_days", None),
			"start_date": parse_datetime(request.data.get("start_date", None)),
			"end_date": parse_datetime(request.data.get("end_date", None)),
			"training": request.data.get("training", None),
			"reimbursement": request.data.get("reimbursement", None),
			"reimbursement_other": request.data.get("reimbursement_other", None),
			"supervision": request.data.get("supervision", None),
			"other": request.data.get("other", None),
			"paid_job": request.data.get("paid_job", None),
			"notes": request.data.get("notes", None),
			"filter_color": request.data.get("filter_color", None),
			"youth": request.data.get("youth", None),
			"english": request.data.get("english", None),
			"disability": request.data.get("disability", None),
			"mental": request.data.get("mental", None),
			"region_of_placement_list": request.data.getlist("region_of_placement_list[]", None) if hasattr(request.data, 'getlist') else request.data.get("region_of_placement_list", []),
			"days_list": request.data.getlist("days_list[]", None) if hasattr(request.data, 'getlist') else request.data.get("days_list", []),
			"time_list": request.data.getlist("time_list[]", None) if hasattr(request.data, 'getlist') else request.data.get("time_list", []),
			"activities_driving_list": request.data.getlist("activities_driving_list[]", None) if hasattr(request.data, 'getlist') else request.data.get("activities_driving_list", []),
			"activities_administration_list": request.data.getlist("activities_administration_list[]", None) if hasattr(request.data, 'getlist') else request.data.get("activities_administration_list", []),
			"activities_mantinance_list": request.data.getlist("activities_mantinance_list[]", None) if hasattr(request.data, 'getlist') else request.data.get("activities_mantinance_list", []),
			"activities_home_cares_list": request.data.getlist("activities_home_cares_list[]", None) if hasattr(request.data, 'getlist') else request.data.get("activities_home_cares_list", []),
			"activities_technology_list": request.data.getlist("activities_technology_list[]", None) if hasattr(request.data, 'getlist') else request.data.get("activities_technology_list", []),
			"activities_event_list": request.data.getlist("activities_event_list[]", None) if hasattr(request.data, 'getlist') else request.data.get("activities_event_list", []),
			"activities_hospitality_list": request.data.getlist("activities_hospitality_list[]", None) if hasattr(request.data, 'getlist') else request.data.get("activities_hospitality_list", []),
			"activities_support_list": request.data.getlist("activities_support_list[]", None) if hasattr(request.data, 'getlist') else request.data.get("activities_support_list", []),
			"activities_financial_list": request.data.getlist("activities_financial_list[]", None) if hasattr(request.data, 'getlist') else request.data.get("activities_financial_list", []),
			"activities_other_list": request.data.getlist("activities_other_list[]", None) if hasattr(request.data, 'getlist') else request.data.get("activities_other_list", []),
			"activities_sport_list": request.data.getlist("activities_sport_list[]", None) if hasattr(request.data, 'getlist') else request.data.get("activities_sport_list", []),
			"activities_group_list": request.data.getlist("activities_group_list[]", None) if hasattr(request.data, 'getlist') else request.data.get("activities_group_list", []),
			"attachments": attachment_path,
		}

		for bool_field in ["criminal", "transport", "wheelchair", "toilet", "stairs", "home", "oneoff", "paid_job", "youth", "english", "disability", "mental"]:
			data[bool_field] = parse_bool(data.get(bool_field))

		try:
			role = Role.objects.get(id=id)
			for key, value in data.items():
				if value is not None:
					setattr(role, key, value)
			role.save()
			add_comment(3, role.id, request.data.get("comment", None), request.admin) # 3 for Role
			return Response({"message": "Role updated", "id": role.id}, status=200)
		except Role.DoesNotExist:
			return Response({"error": "Role not found"}, status=404)
	except Exception as e:
		return Response({"error": str(e)}, status=400)