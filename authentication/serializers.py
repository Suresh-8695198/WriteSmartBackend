# authentication/serializers.py

from rest_framework import serializers

class ImageUploadSerializer(serializers.Serializer):
    image = serializers.ImageField()


class StudentLoginSerializer(serializers.Serializer):
    register_number = serializers.CharField(max_length=20)
    dob = serializers.DateField()
