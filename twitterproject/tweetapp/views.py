# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework import status
from .models import *
from .serializers import TweetsSerializer, UserSerializer


class TweetsListAPIView(ListAPIView):
    queryset = Tweets.objects.all()
    serializer_class = TweetsSerializer


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



