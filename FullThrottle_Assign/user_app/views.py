from django.shortcuts import render
from rest_framework import viewsets,status
from user_app.models import Profile,Activity,Member
from  user_app.serializers import ProfileSerializer,ActivitySerializer,MemberSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.generics import ListAPIView

class ProfileViewset(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
