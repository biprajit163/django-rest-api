from rest_framework import serializers
from .models import User

# Make Serializers for each model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'blogs']
