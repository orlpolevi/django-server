from rest_framework import serializers 
from Users.models import User

class UserSerialzier(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = (	"name", "lastName" ,"userType", "userStatus")