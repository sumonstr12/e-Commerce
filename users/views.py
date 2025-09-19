
from django.contrib.auth import authenticate, get_user_model

from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

from .serializers import UserRegistrationSerializer, UserProfileSerialier

import random

from django.core.mail import send_mail
from Ecommerce_Backend.settings import EMAIL_HOST_USER

# Create your views here.


User = get_user_model()

class UserRegistrationView(APIView):
    def post(self,request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "status" : "success",
                    "message" : "User registration successfull."
                }, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.error_messages, status=status.HTTP_400_BAD_REQUEST
        )

class UserLoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(request, email=email, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            response = Response(
                {
                    "success":"success",
                    "message":"User login SuccessFull.",
                    "access token" : str(refresh.access_token),
                    "refresh token" : str(refresh)
                }, status=status.HTTP_200_OK
                
            )

            refresh_token = str(refresh)
            # Add refresh_token on cookie
            response.set_cookie(
                key="refresh_token",
                value=refresh_token,
                max_age=30 * 24 *60 * 60,
                httponly=True,
                secure=True,
                samesite="strict"
            )

            return response
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    

class SendOtpView(APIView):
    def post(self, request):
        email = request.data.get("email")
        user = User.objects.get(email=email)
        if not email or not User.objects.filter(email=email).exists():
            return Response(
                {
                    "status" : "failed",
                    "message" : "Provide valid email",
                }, status=status.HTTP_400_BAD_REQUEST
            )
        
        otp = str(random.randint(1000, 9999))
        user.otp = otp
        user.save()

        try:
            send_mail(
                subject="Your Otp-",
                from_email= "E-commerce<amajonshops@gmail.com>",
                message= f"your otp is {otp}",
                recipient_list=[email],
                fail_silently=False
            )
        except Exception as e:
            return Response(
                {
                    "message" : f"Failed to send otp {otp}"
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        return Response(
            {
                "status" : "success",
                "message" : "Otp sent successful.",
                "otp" : otp
            }, status=status.HTTP_200_OK
        )

class VerifyOtpView(APIView):
    def post(self, request):
        email = request.data.get("email")
        otp = request.data.get("otp")

        
        if not User.objects.filter(email=email).exists():
            return Response(
                {
                    "status" : "Failed",
                    "message" : "Provide valid Email"
                }, status=status.HTTP_401_UNAUTHORIZED
            )
        try:
            user = User.objects.get(email=email, otp=otp)
            user.otp = None
            token = str(RefreshToken.for_user(user).access_token)
            return Response(
                {
                    "status" : "success",
                    "message": "Otp Verify Successful",
                    "token" : token
                }, status=status.HTTP_202_ACCEPTED
            )
        except User.DoesNotExist:
            return Response(
                {
                    "status" : "Failed",
                    "message" : "Action Failed"
                }, status=status.HTTP_401_UNAUTHORIZED
            )


class ResetPasswordView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        password = request.data.get("password")
        print(request.user)
        user = request.user
        user.set_password(password)
        user.save()

        if not password:
            return Response(
                {
                    "status" : "failed",
                    "message" : "Provied Password"
                }, status=status.HTTP_204_NO_CONTENT
            )

        return Response(
            {
                "status" : "success",
                "message" : "Password Reset Successful"
            },status=status.HTTP_200_OK
        )

class UpadateProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        user = request.user
        serializer = UserProfileSerialier(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "status" : "success",
                    "message" : "Profile Updated Successful",
                }
            )

class UserProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        user = request.user
        data = UserProfileSerialier(user).data

        return Response(
            {
                "status" : "success",
                "message" : "Request Successful",
                "data" : data
            },status=status.HTTP_200_OK
        )


class UserLogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        refresh_token = request.COOKIES.get("refresh_token")
        print(refresh_token)
        if not refresh_token:
            return Response({
                "status" : "Failed",
                "message" : "Refres Token Required"
            }, status=status.HTTP_400_BAD_REQUEST)
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
        except Exception:
            return Response(
                {
                    "status" : "Failed"
                }
            )
        
        
        return Response(
            {
                "status" : "success",
                "message" : "Logout Succesful"
            }, status=status.HTTP_200_OK
        )