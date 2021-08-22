from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User
from .models import *
from .serializers import *
import datetime
import json
import os
import codecs
from django.template.loader import get_template
from django.template import Template, Context
from django.contrib.auth.hashers import check_password, make_password


def getWishStatus(request):
    statuses = Wish_status.objects.all()
    status_list = []
    for instance in statuses:
        print(instance.status)
        status_list.append(instance.status)
    print(status_list)
    return JsonResponse({'status': status_list})

class wishList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        print(request.user)
        requestor = Requestor.objects.filter(user=request.user).first()
        if request.user.is_staff:
            wish = User_wish.objects.all()
        else: 
            wish = User_wish.objects.filter(requestor=requestor).all()
        serializer = UserWishSerializer(
            wish, many=True, context={'request': request})
        return Response(serializer.data)

class writeWishList(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        try:
            print(request.body)
            data = json.loads(request.body)
            User_wish.objects.create(
            requestor = Requestor.objects.filter(user = request.user).get(),
            date = data['date'],
            status = Wish_status.objects.filter(status = 'Draft').get(),
            wish_type = data['wish_type'],
            subject = data['subject'],
            territory = data['territory'],
            asignee = data['asignee'],
            version = data['version'],
            description = data['description'])
            return JsonResponse({'server': 'success'})
        except BaseException as e:
            print(e)
            return JsonResponse({'server': 'fail'})

class singleWishList(APIView):
    permission_classes = (AllowAny,)

    def put(self, request, wish_id):
        data = json.loads(request.body)
        print(data['status'])

        wish = User_wish.objects.filter(id=wish_id).get()
        try:
            status = Wish_status.objects.filter(status = data['status']).get()
            wish.status = status 
            wish.save()
            res = JsonResponse({'server': 'success'})
            res.status_code = 200
            return res
        except BaseException as e:
            print(e)
            Wish_status.objects.create(status = data['status'])
            status = Wish_status.objects.filter(status = data['status']).get()
            wish.status = status 
            wish.save()
            res = JsonResponse({'server': 'new column created'})
            res.status_code = 200
            return res
    def post(self, request, wish_id):
        try:
            data = json.loads(request.body)
            print(data)
            wish = User_wish.objects.filter(id=wish_id).get()
            wish.date = data['date']
            wish.wish_type = data['wish_type']
            wish.subject = data['subject']
            wish.territory = data['territory']
            wish.asignee = data['asignee']
            wish.version = data['version']
            wish.description = data['description']
            wish.save()
            res =  JsonResponse({'server': 'success'})
            res.status_code =200
            return res
        except BaseException as e:
            print(e)
            res = JsonResponse({"message": "server error"})
            res.status_code = 500
            return res
    def delete(self, request, wish_id):
        try:
            wish = User_wish.objects.filter(id=wish_id).get()
            wish.delete()
            res = JsonResponse({'server': 'success'})
            res.status_code = 200
            return res
        except BaseException as e:
            print(e)
            res = JsonResponse({"message": "server error"})
            res.status_code = 500
            return res


class createStatus(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        try:
            data = json.loads(request.body)
            Wish_status.objects.create(status = data['status'])
            res = JsonResponse({'server': 'new column created'})
            res.status_code = 200
            return res
        except BaseException as e:
                print(e)
                res = JsonResponse({"message": "server error"})
                res.status_code = 500
                return res

