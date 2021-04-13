from django.urls import path
from django.conf.urls import include
from . import views
from rest_framework import routers
from .views import UserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
 path('', include(router.urls)),
 path('user/',views.GetUser.as_view()),
 path('userinfo/',views.UserInfo.as_view()),
 ### Property Management 
 path('properties/',views.PropertyDisplay.as_view()),
 path('plots/',views.PlotDisplay.as_view()),
 path('commercial/',views.CommercialDisplay.as_view()),
 path('CreateAd/',views.CreateAd.as_view()),
 path('AD/<int:pk>/',views.AdDisplay.as_view()),
 path('Delete/<int:pk>/',views.DeleteAd.as_view()),
 path('Edit/<int:pk>/',views.EditAd.as_view()),
 path('advertisements/',views.AdvertisementDisplay.as_view()),
 path('searchAds/',views.SearchAds.as_view()),
 path('dashboard/',views.Dashboard.as_view()),
 path('Like/',views.CreateLike.as_view()),
 path('LikedAds/',views.LikedAds.as_view()),
 path('Liked/<str:pk>/',views.Liked.as_view()),
 path('Unlike/<int:pk>/',views.DeleteLiked.as_view()),
 path('Latest/',views.LatestAds.as_view()),
 path('MostViewed/',views.MostViewed.as_view()),
 path('Featured/',views.Featured.as_view()),
 path('Blogs/',views.ListBlogs.as_view()),
 path('Blog/<int:pk>',views.BlogDetails.as_view()),
 path('PriceIndex/',views.PriceIndex.as_view()),
 path('CityIndex/<int:pk>',views.CityIndex.as_view()),
 path('City/<int:pk>/',views.CitySpecificIndex.as_view()),
 path('Cities/',views.CityAllIndex.as_view()),
 path('Products/',views.Products.as_view()),
 path('Product/<int:pk>/',views.ProductDisplay.as_view()),
 path('Rating/<int:pk>/',views.RatingDisplay.as_view()),
 path('CreateRating/',views.CreateRating.as_view()),
  ]
