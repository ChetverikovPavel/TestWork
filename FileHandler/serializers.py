from rest_framework import serializers
from .models import File


class FilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        exclude = ('id',)

class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()
    

    def create(self, validated_data):
        return File.objects.create(**validated_data)