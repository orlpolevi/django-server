from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

from .models import User
from .serializers import UserSerialzier
# Create your views here.

#to test on the server
def user_detail_view(request):
	obj = User.objects.get(id=4)
	context = {
		"object": obj
	}
	return render(request, "Users/detail.html", context)

#rest api connection 

@api_view(['GET', 'POST', 'DELETE'])
def user_get_by_id(request, pk):
	#object retrival
	try:
		obj = User.objects.get(pk=pk)
	except Users.DoesNotExist:
		return JsonResponse({'message': 'does not exist'},  status=status.HTTP_404_NOT_FOUND)
	
	#GET
	if request.method == 'GET':
		user_serializer = UserSerialzier(obj)
		return JsonResponse(user_serializer.data) 
		 
 
