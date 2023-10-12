from django.shortcuts import get_object_or_404
from .models import Student
from .serializers import StudentSerializer, UserSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User



@api_view(['POST'])
def login(request):
     try:
          user = User.objects.get(username=request.data['name'])
     except User.DoesNotExist:
          return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)
     
     if not user.check_password(request.data['password']):
          return Response({"detail": "Invalid password."}, status=status.HTTP_401_UNAUTHORIZED)
     
     token, created = Token.objects.get_or_create(user=user)
     serializer = UserSerializer(user)
     return Response({"token": token.key, "user": serializer.data})
 

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user, created = User.objects.get_or_create(username=request.data['username'])
        if created:
            user.set_password(request.data['password'])
            user.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key, "user": serializer.data})
        else:
            return Response({"error": "User with this username already exists."}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def test_token(request):
    return Response({})

class student_list(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class student_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer