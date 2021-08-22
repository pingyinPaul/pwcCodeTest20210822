from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
import os
import codecs
from rest_framework import serializers
import datetime
from ckeditor.fields import RichTextField
# Create your models here.
######
import ast


from typing import Iterable


class ListField(models.TextField):
    """
    A custom Django field to represent lists as comma separated strings
    """

    def __init__(self, *args, **kwargs):
        self.token = kwargs.pop('token', ',')
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        kwargs['token'] = self.token
        return name, path, args, kwargs

    def to_python(self, value):

        class SubList(list):
            def __init__(self, token, *args):
                self.token = token
                super().__init__(*args)

            def __str__(self):
                return self.token.join(self)

        if isinstance(value, list):
            return value
        if value is None:
            return SubList(self.token)
        return SubList(self.token, value.split(self.token))

    def from_db_value(self, value, expression, connection):
        return self.to_python(value)

    def get_prep_value(self, value):
        if not value:
            return
        assert(isinstance(value, Iterable))
        return self.token.join(value)

    def value_to_string(self, obj):
        value = self.value_from_object(obj)
        return self.get_prep_value(value)

class Requestor(models.Model): 
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True, default=None)
    name = models.CharField(max_length=50, blank=True,)
    def __str__(self):
        return str(self.name) 

class Wish_status(models.Model):
    status = models.CharField(default="Draft", max_length =100)
    def __str__(self):
            return str(self.status) 

class User_wish(models.Model):
    requestor = models.ForeignKey(Requestor, on_delete=models.CASCADE, null=True)
    date = models.DateField()
    status = models.ForeignKey(Wish_status, on_delete=models.CASCADE, null=True, default=1)
    wish_type = models.CharField(default="Wishlist", choices=[
        ('Wishlist', 'Wishlist'),
        ('Other', 'Other'),

    ], max_length=100)
    subject = models.CharField(max_length=1000, blank=True)
    territory = models.CharField(default="PwC Mekong", choices=[
        ('PwC Mekong', 'PwC Mekong'),
        ('Other', 'Other'),

    ], max_length=100)
    asignee = models.CharField(max_length=50, blank=True)
    version = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=3000, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.asignee) + " " + "-" + " " + str(self.subject) + "/" + str(self.requestor)

