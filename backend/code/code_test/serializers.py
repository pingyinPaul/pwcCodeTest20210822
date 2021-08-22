from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import AnonymousUser, User
import datetime
import pytz
from django.db.models import Sum, Avg
import time
from .models import *
class RequestorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requestor
        fields = '__all__'
        

class WishStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wish_status

        fields = '__all__'
class UserWishSerializer(serializers.ModelSerializer):
    status = WishStatusSerializer(read_only=True)
    requestor = serializers.SerializerMethodField()
    def get_requestor(self, obj):
        requestor = Requestor.objects.filter(user=obj.requestor).get()
        return requestor.name
    class Meta:
        model = User_wish
        fields = '__all__'



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)


class UserSerializerWithToken(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('token', 'username', 'password')


