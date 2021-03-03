from django.shortcuts import render
from rest_framework import generics,permissions,status,viewsets
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated,AllowAny
from .models import Ad,Saved,ItemAD
from .serializers import AdSerializer ,UserSerializer,SavedSerializer,ItemSerializer
from rest_framework.response import Response
from rest_framework.decorators import action , api_view
from rest_framework.authentication import TokenAuthentication,SessionAuthentication
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate,login,logout
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
import json

### User Management ###
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserInfo(generics.ListAPIView):
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication, ]
    
    def get_queryset(self):
        return User.objects.filter(email = self.request.user.email)

class GetUser(generics.ListAPIView):
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    def get_queryset(self):
        return User.objects.filter(email=self.request.user.email)    

### Property Management Views ###
class PropertyDisplay(generics.ListAPIView):
    queryset = Ad.objects.filter(Type='property')
    serializer_class = AdSerializer

class AdvertisementDisplay(generics.ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    filter_backends = (SearchFilter,OrderingFilter)
    search_fields = ('^Location','=User__username','^City','=Size','=Units','=Price','=Purpose','=Type','=Construction_status','=Beds','=Baths')

class SearchAds(generics.ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    filter_backends = (SearchFilter,OrderingFilter)
    search_fields = ('@Location','@User__username','@City','@Size','@Units','@Price','@Purpose','@Type','@Construction_status','@Beds','@Baths')


class PlotDisplay(generics.ListAPIView):
    queryset = Ad.objects.filter(Type='plot')
    serializer_class = AdSerializer

class CommercialDisplay(generics.ListAPIView):
    queryset = Ad.objects.filter(Type='commercial')
    serializer_class = AdSerializer

class Dashboard(generics.ListAPIView):
    serializer_class = AdSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return Ad.objects.filter(User=self.request.user)


class CreateAd(generics.CreateAPIView):
    serializer_class = AdSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return Ad.objects.all(user='1')

    def perform_create(self,serializer):
        serializer.save(User=self.request.user)
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

class CreateLike(generics.CreateAPIView):
    serializer_class = SavedSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)
        return JsonResponse({'response':'Advertisement Liked Successfully'},status=201)

class LikedAds(generics.ListAPIView):
    serializer_class = SavedSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    def get_queryset(self):
        return Saved.objects.filter(user=self.request.user)

class DeleteLiked(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SavedSerializer
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Saved.objects.filter(id=pk)
    
    def perform_delete(self,serializer):
        serializer.delete()
    
class Liked(generics.RetrieveAPIView):
    serializer_class = SavedSerializer
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated, ]
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Saved.objects.filter(Ad=pk,user=self.request.user)
     
class LatestAds(generics.ListAPIView):
    serializer_class = AdSerializer
    queryset = Ad.objects.all().order_by('-Time')[:6]
class MostViewed(generics.ListAPIView):
    serializer_class = AdSerializer
    queryset = Ad.objects.all().order_by('Views')[:6]
class Featured(generics.ListAPIView):
    serializer_class = AdSerializer
    queryset = Ad.objects.filter(Featured=True).order_by('id')[:6]
    
### e-Commerce Views ###
class Items(generics.ListAPIView):
    serializer_class = ItemSerializer
    authentication_classes = [TokenAuthentication,]
    permission_class = [IsAuthenticated,]
    queryset = ItemAD.objects.all()

class DashboardItems(generics.ListAPIView):
    serializer_class = ItemSerializer
    authentication_classes = [TokenAuthentication,]
    permission_class = [IsAuthenticated,]
    def get_queryset(self):
        return ItemAD.objects.filter(user=self.request.user)
        
class CreateItem(generics.CreateAPIView):
    serializer_class = ItemSerializer
    authentication_classes = [TokenAuthentication,]
    permission_class = [IsAuthenticated,]
    
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)
        return JsonResponse({'response':'Item Added Successfully'},status=201)

    
class EditItem(generics.RetrieveUpdateAPIView):
    serializer_class = ItemSerializer
    authentication_classes = [TokenAuthentication,]
    permission_class = [IsAuthenticated,]
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return ItemAD.objects.filter(id=pk,user=self.request.user)

class DeleteItem(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializer
    authentication_classes = [TokenAuthentication,]
    permission_class = [IsAuthenticated,]
    def get_queryset(self):
        pk = self.kwargs['pk']
        return ItemAD.objects.filter(id=pk,user=self.request.user)
    def perform_delete(self,serializer):
        serializer.delete()

class ItemDisplay(generics.RetrieveAPIView):
    serializer_class = AdSerializer
    authentication_classes = [TokenAuthentication,]
    permission_class = [IsAuthenticated,]

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Ad.objects.filter(id=pk)
                                                                                    