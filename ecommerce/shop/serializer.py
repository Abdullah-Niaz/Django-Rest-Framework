from rest_framework import serializers
from .models import StudentData

class studentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    phone = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=100)
