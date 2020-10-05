from django.shortcuts import render
from .serializers import UserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import FileUploadParser
from .serializers import PictureSerializer
from django.views.decorators.csrf import csrf_exempt
from .models import Picture

# Create your views here.

class UserView(APIView):
    permission_classes = [AllowAny]
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class PictureUploadView(APIView):
    parser_class = (FileUploadParser,)
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        pictures = Picture.objects.filter(creator=request.user)
        serializer = PictureSerializer(pictures, many=True)
        return Response(serializer.data)


    def post(self, request, *args, **kwargs):
        creator = request.user
        file_serializer = PictureSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save(creator=creator)
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)          

        