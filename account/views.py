from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .serializers import (
    RegisterUserSerializer, ChangePasswordSerializer, ProfileSerializer
    )
from .utils import get_tokens_for_user
from .models import User


class RegisterView(APIView):
    
    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid(): 
            user = serializer.save()
           # user = User.objects.get(email=serializer.validated_data["email"])
            tokens = get_tokens_for_user(user)
            return Response({"username":serializer.validated_data['username'], **tokens}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ChangePasswordView(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request):
        serializer = ChangePasswordSerializer(context={'request': request}, data=request.data)
        if serializer.is_valid():
            request.user.set_password(serializer.validated_data['new_password'])
            request.user.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = get_object_or_404(User, email=request.user.email)
        serializer = ProfileSerializer(user)
        return Response(serializer.data)

    def put(self, request):
        user = get_object_or_404(User, email=request.user.email)
        serializer = ProfileSerializer(user, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request):
        user = get_object_or_404(User, email=request.user.email)
        serializer = ProfileSerializer(user, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        user = get_object_or_404(User, username=request.user)
        User.delete(user)
        return Response(status=status.HTTP_204_NO_CONTENT)
