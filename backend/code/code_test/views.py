import json

from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User, update_last_login
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny

from rest_framework.response import Response

# Create your views here.
from rest_framework import viewsets, filters
from rest_framework.views import APIView

from .serializers import *
from .models import *
from datetime import datetime, timezone

class UserWishViewSet(viewsets.ModelViewSet):
    queryset = User_wish.objects.all()
    serializer_class = UserWishSerializer

