from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import UserSerializer
from services.email_service import EmailService
from services.otp_service import OTPService

# Create your views here.

class SignUpView(APIView):
    def post(self,request,*args,**kwargs):
        serializer = UserSerializer()

        if serializer.is_valid():
            username = serializer.validate['username']
            email = serializer.validate['email']
            password = serializer.validate['password']

            User =  get_user_model()
            user = User(username=username,email=email,password=make_password(password))
            user.save()

            otp_service =  OTPService()
            otp =  otp_service.generate_otp(email)

            email_service =  EmailService()
            email_service.sent_otp_email(email,otp)

            return Response({'messge':'User created successfully.Otp send to email'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
