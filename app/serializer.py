from rest_framework import serializers
from django.contrib.auth.models import User


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validate_data):
        user = User.objects.create_user(
            username=validate_data['username'],
            password=validate_data['password'],
            first_name=validate_data['first_name'],
            last_name=validate_data['last_name']
        )
        return user


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
