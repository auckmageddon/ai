from tasks import get_steam_account_for_name
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api_v2 import ProfileSerializer
import json

@api_view(['GET'])
def get_steam_account(request):
	name = request.GET.get('name', '')
	if name is not '':
		profile = get_steam_account_for_name(name)
		if profile is not None:
			serialized = ProfileSerializer(profile)
			return Response(serialized.data)
	return Response(status=400)