from django.shortcuts import render
from rest_framework import generics,permissions,status
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated,AllowAny
from .models import Ad
from .serializers import AdSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication,SessionAuthentication
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate,login,logout
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

class PropertyDisplay(generics.ListAPIView):
    queryset = Ad.objects.filter(Type='property')
    serializer_class = AdSerializer

class PlotDisplay(generics.ListAPIView):
    queryset = Ad.objects.filter(Type='plot')
    serializer_class = AdSerializer

class CommercialDisplay(generics.ListAPIView):
    queryset = Ad.objects.filter(Type='commercial')
    serializer_class = AdSerializer

class CreateAd(generics.CreateAPIView):
    serializer_class = AdSerializer

    def get_queryset(self):
        return Ad.objects.all(user='1')

    def perform_create(self,serializer):
        serializer.save()
        return JsonResponse({'response':'Advertisement Created Successfully'},status=201)

        

class AdDisplay(generics.RetrieveAPIView):
    serializer_class = AdSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Ad.objects.filter(id=pk)

class DeleteAd(generics.RetrieveDestroyAPIView):
    serializer_class = AdSerializer
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Ad.objects.filter(id=pk)
    def perform_delete(self,serializer):
        serializer.delete()
    

class EditAd(generics.RetrieveUpdateAPIView):
    serializer_class = AdSerializer
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Ad.objects.filter(id=pk)
