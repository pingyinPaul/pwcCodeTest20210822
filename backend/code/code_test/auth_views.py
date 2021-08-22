from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.http import JsonResponse
import json
import requests
import random
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django_email_verification import send_email
from django.db.models import Max, Value, Q
from datetime import date, timedelta
from datetime import datetime



def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        return token



class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class check_is_logged_in(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = User.objects.filter(username=request.user).first()
        #group = user.groups.first()
        patient = Patient.objects.filter(user=user).first()
        doctor = Doctor.objects.filter(user=user).first()
        if patient is not None:
            user_group = "patient"
        elif doctor is not None:
            user_group = "doctor"
        elif request.user.is_staff:
            user_group = "admin"
        else:
            user_group = ''

        wechat_img = ""
        wechat = Wechat_id.objects.filter(user=user).first()

        if wechat is not None:
            wechat_img = wechat.wechat_img

        if patient is not None:
            status_group = patient.group
        else:
            status_group = ''

        content = {'message': "success", "username": user.username,
                   "email": user.email, "id": user.id,
                   "user_group": user_group,
                   "status_group": status_group, "wechat_img": wechat_img}
        # print(content)
        return JsonResponse(content)




def signup(request):
    if request.method == "POST":
        # try:
        request_data = json.loads(request.body.decode('utf-8'))
        username = request_data["username"]
        email = request_data["email"]
        password = request_data["password"]

        # check if there is some username
        user = User.objects.filter(username=username).first()
        if user is not None:
            res = JsonResponse({"message": "用戶名稱已存在"})
            res.status_code = 400
            return res
        else:
            if len(password) > 30 or len(password) < 8:
                res = JsonResponse({"message": "密碼需大於8個字與少於30個字"})
                res.status_code = 400
                return res
            elif any(char.isupper() for char in password) and any(char.islower() for char in password) and any(char.isdigit() for char in password):
                user = User.objects.create_user(
                    username=username, email=email, password=password)
                patient = Patient.objects.create(
                    user=user,
                    email=user.email,
                )
                patient.atop_id = "ATOP" + str(patient.id).zfill(6)
                patient.save()
                content = {'message': "success", "username": user.username}
                return JsonResponse(content)
            else:
                res = JsonResponse({"message": "密碼需同時含有大楷字母,小楷字母及數字"})
                res.status_code = 400
                return res

