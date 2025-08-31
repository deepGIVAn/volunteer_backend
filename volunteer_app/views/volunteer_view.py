from volunteer_app.decorators import admin_token_required
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
import os
import re
from datetime import datetime
from django.conf import settings
from volunteer_app.model import Volunteer
from .organisation_view import parse_datetime
from volunteer_app.serializers import VolunteerSerializer

@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
@admin_token_required
def create_volunteer(request):
	try:
		data = {
			"title": request.data.get("title", None),
			"first_name": request.data.get("first_name", None),
			"last_name": request.data.get("last_name", None),
			"email": request.data.get("email", None),
			"street": request.data.get("street", None),
			"city": request.data.get("city", None),
			"post_code": request.data.get("post_code", None),
			"phone": request.data.get("phone", None),
			"year_of_birth": request.data.get("year_of_birth", None),
			"date_added": parse_datetime(request.data.get("date_added", None)),
			"hours": request.data.get("hours", None),
			"qualification": request.data.get("qualification", None),
			"work_experience": request.data.get("work_experience", None),
			"skills": request.data.get("skills", None),
			"health": request.data.get("health", None),
			"other_information": request.data.get("other_information", None),
			"notes": request.data.get("notes", None),
			"languages": request.data.get("languages", None),
			"type_of_work_list": request.data.getlist("type_of_work_list[]", None) if hasattr(request.data, 'getlist') else request.data.get("type_of_work_list", []),
			"region_of_placement_list": request.data.getlist("region_of_placement_list[]", None) if hasattr(request.data, 'getlist') else request.data.get("region_of_placement_list", []),
			"refer_from_list": request.data.getlist("refer_from_list[]", None) if hasattr(request.data, 'getlist') else request.data.get("refer_from_list", []),
			"days_list": request.data.getlist("days_list[]", None) if hasattr(request.data, 'getlist') else request.data.get("days_list", []),
			"time_list": request.data.getlist("time_list[]", None) if hasattr(request.data, 'getlist') else request.data.get("time_list", []),
			"labour_list": request.data.getlist("labour_list[]", None) if hasattr(request.data, 'getlist') else request.data.get("labour_list", []),
			"status": request.data.get("status", None),
			"color": request.data.get("color", None),
			"transport_list": request.data.getlist("transport_list[]", None) if hasattr(request.data, 'getlist') else request.data.get("transport_list", []),
			"review_date": parse_datetime(request.data.get("review_date", None)),
			"gender": request.data.get("gender", None),
			"ethnic_origin_list": request.data.getlist("ethnic_origin_list[]", None) if hasattr(request.data, 'getlist') else request.data.get("ethnic_origin_list", []),
			"activities_list": request.data.getlist("activities_list[]", None) if hasattr(request.data, 'getlist') else request.data.get("activities_list", []),
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
		}
		
		volunteer = Volunteer.objects.create(**{k: v for k, v in data.items() if v is not None})
		return Response({"message": "Volunteer created successfully", "id": volunteer.id}, status=201)
	except Exception as e:
		return Response({"error": str(e)}, status=400)

@api_view(['GET'])
@admin_token_required
def get_all_volunteers(request):
	volunteers = Volunteer.objects.all()
	serializer = VolunteerSerializer(volunteers, many=True)
	return Response(serializer.data)

@api_view(['GET'])
@admin_token_required
def get_volunteer(request, id):
	try:
		volunteer = Volunteer.objects.get(id=id)
		serializer = VolunteerSerializer(volunteer)
		return Response(serializer.data, status=200)
	except Volunteer.DoesNotExist:
		return Response({"error": "Volunteer not found"}, status=404)

@api_view(['DELETE'])
@admin_token_required
def delete_volunteer(request, id):
	try:
		volunteer = Volunteer.objects.get(id=id)
		volunteer.deleted_at = datetime.now()
		volunteer.isdeleted = True
		volunteer.save()
		return Response({"message": "Volunteer deleted"}, status=200)
	except Volunteer.DoesNotExist:
		return Response({"error": "Volunteer not found"}, status=404)

@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
@admin_token_required
def update_volunteer(request, id):
	try:
		data = {
			"title": request.data.get("title", None),
			"first_name": request.data.get("first_name", None),
			"last_name": request.data.get("last_name", None),
			"email": request.data.get("email", None),
			"street": request.data.get("street", None),
			"city": request.data.get("city", None),
			"post_code": request.data.get("post_code", None),
			"phone": request.data.get("phone", None),
			"year_of_birth": request.data.get("year_of_birth", None),
			"date_added": parse_datetime(request.data.get("date_added", None)),
			"hours": request.data.get("hours", None),
			"qualification": request.data.get("qualification", None),
			"work_experience": request.data.get("work_experience", None),
			"skills": request.data.get("skills", None),
			"health": request.data.get("health", None),
			"other_information": request.data.get("other_information", None),
			"notes": request.data.get("notes", None),
			"languages": request.data.get("languages", None),
			"type_of_work_list": request.data.getlist("type_of_work_list[]", None) if hasattr(request.data, 'getlist') else request.data.get("type_of_work_list", []),
			"region_of_placement_list": request.data.getlist("region_of_placement_list[]", None) if hasattr(request.data, 'getlist') else request.data.get("region_of_placement_list", []),
			"refer_from_list": request.data.getlist("refer_from_list[]", None) if hasattr(request.data, 'getlist') else request.data.get("refer_from_list", []),
			"days_list": request.data.getlist("days_list[]", None) if hasattr(request.data, 'getlist') else request.data.get("days_list", []),
			"time_list": request.data.getlist("time_list[]", None) if hasattr(request.data, 'getlist') else request.data.get("time_list", []),
			"labour_list": request.data.getlist("labour_list[]", None) if hasattr(request.data, 'getlist') else request.data.get("labour_list", []),
			"status": request.data.get("status", None),
			"color": request.data.get("color", None),
			"transport_list": request.data.getlist("transport_list[]", None) if hasattr(request.data, 'getlist') else request.data.get("transport_list", []),
			"review_date": parse_datetime(request.data.get("review_date", None)),
			"gender": request.data.get("gender", None),
			"ethnic_origin_list": request.data.getlist("ethnic_origin_list[]", None) if hasattr(request.data, 'getlist') else request.data.get("ethnic_origin_list", []),
			"activities_list": request.data.getlist("activities_list[]", None) if hasattr(request.data, 'getlist') else request.data.get("activities_list", []),
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
		}
		try:
			volunteer = Volunteer.objects.get(id=id)
			for key, value in data.items():
				if value is not None:
					setattr(volunteer, key, value)
			volunteer.save()
			return Response({"message": "Volunteer updated", "id": volunteer.id}, status=200)
		except Volunteer.DoesNotExist:
			return Response({"error": "Volunteer not found"}, status=404)
	except Exception as e:
		# print(e)
		return Response({"error": str(e)}, status=400)