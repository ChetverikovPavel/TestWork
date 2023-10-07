from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import FilesSerializer, FileUploadSerializer
from .models import File
from .tasks import file_handler

# Create your views here.

@api_view()
def FilesListView(request):    
    files = File.objects.all()
    serializer = FilesSerializer(files, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def FileUploadView(request):
    serializer = FileUploadSerializer(data = request.data)
    serializer.is_valid()
    updatedFile = serializer.save()
    file_handler.delay(updatedFile.id)
    
    return Response(data=serializer.data, status=201)