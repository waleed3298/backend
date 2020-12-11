from django.urls import path
from django.conf.urls import include
from . import views
from rest_framework import routers
from .views import UserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
 path('', include(router.urls)),
 path('search/',views.SearchAds.as_view()),
 path('properties/',views.PropertyDisplay.as_view()),
 path('plots/',views.PlotDisplay.as_view()),
 path('commercial/',views.CommercialDisplay.as_view()),
 path('CreateAd/',views.CreateAd.as_view()),
 path('AD/<int:pk>/',views.AdDisplay.as_view()),
 path('Delete/<int:pk>/',views.DeleteAd.as_view()),
 path('Edit/<int:pk>/',views.EditAd.as_view()),
 path('advertisements/',views.AdvertisementDisplay.as_view()),
 path('dashboard/',views.Dashboard.as_view()),
 ]
