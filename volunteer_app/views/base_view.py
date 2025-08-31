from rest_framework.decorators import api_view
from data import *
from rest_framework.response import Response

@api_view(['GET'])
def get_preset(request, type):
	if type == "regions":
		return Response(get_regions_list(), status=200)
	elif type == "services":
		return Response(get_services_list(), status=200)
	elif type == "days":
		return Response(get_days_list(), status=200)
	elif type == "time":
		return Response(get_time_list(), status=200)
	elif type == "activities_driving_list":
		return Response(get_activities_driving_list(), status=200)
	elif type == "activities_administration_list":
		return Response(get_activities_administration_list(), status=200)
	elif type == "activities_mantinance_list":
		return Response(get_activities_mantinance_list(), status=200)
	elif type == "activities_home_cares_list":
		return Response(get_activities_home_cares_list(), status=200)
	elif type == "activities_technology_list":
		return Response(get_activities_technology_list(), status=200)
	elif type == "activities_event_list":
		return Response(get_activities_event_list(), status=200)
	elif type == "activities_hospitality_list":
		return Response(get_activities_hospitality_list(), status=200)
	elif type == "activities_support_list":
		return Response(get_activities_support_list(), status=200)
	elif type == "activities_financial_list":
		return Response(get_activities_financial_list(), status=200)
	elif type == "activities_other_list":
		return Response(get_activities_other_list(), status=200)
	elif type == "activities_sport_list":
		return Response(get_activities_sport_list(), status=200)
	elif type == "activities_group_list":
		return Response(get_activities_group_list(), status=200)
	else:
		return Response([], status=400)