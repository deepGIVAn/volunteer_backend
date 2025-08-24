from rest_framework.decorators import api_view
from data import get_regions_list, get_services_list
from rest_framework.response import Response

@api_view(['GET'])
def get_preset(request, type):
	if type == "regions":
		return Response(get_regions_list(), status=200)
	elif type == "services":
		return Response(get_services_list(), status=200)
	else:
		return Response([], status=400)