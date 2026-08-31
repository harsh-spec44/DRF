from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegistrationUserSerializer
# Create your views here.
# GMC yukon denali ultimate - black, mercdes g63 amg - grey| blue, rr ghost - blue| brown, 12 cillindri , urus blue, bentley continental grey-black
class LoginAPIView(APIView):
    authentication_classes = []
    permission_classes = []
    
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            token, created = token.objects.get_or_create(user=user)

            return Response({'token':token.key})
        
        return Response({'error': "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class UserRegistration(APIView):
    permission_classes = []
    def post(self, request):
        serializer = RegistrationUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message':'User created successfully'}, status=status.HTTP_201_CREATED)

class LogoutAPIView(APIView):

    def post(self, request):
        request.auth.delete()
        return Response({"msg":'Logout Success'})