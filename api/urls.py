from django.urls import path
from django.conf.urls import include
from . import views
from rest_framework import routers
from .views import UserViewSet

router = routers.DefaultRouter()
router.register("users", UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("user/", views.GetUser.as_view()),
    path("userinfo/", views.UserInfo.as_view()),
    ### Property Management
    path("properties/", views.PropertyDisplay.as_view()),
    path("plots/", views.PlotDisplay.as_view()),
    path("commercial/", views.CommercialDisplay.as_view()),
    path("CreateAd/", views.CreateAd.as_view()),
    path("AD/<int:pk>/", views.AdDisplay.as_view()),
    path("Delete/<int:pk>/", views.DeleteAd.as_view()),
    path("Edit/<int:pk>/", views.EditAd.as_view()),
    path("advertisements/", views.AdvertisementDisplay.as_view()),
    path("searchAds/", views.SearchAds.as_view()),
    path("dashboard/", views.Dashboard.as_view()),
    ### Liked and Most Viewed
    path("Like/", views.CreateLike.as_view()),
    path("LikedAds/", views.LikedAds.as_view()),
    path("Liked/<str:pk>/", views.Liked.as_view()),
    path("Unlike/<int:pk>/", views.DeleteLiked.as_view()),
    path("Latest/", views.LatestAds.as_view()),
    path("MostViewed/", views.MostViewed.as_view()),
    path("Featured/", views.Featured.as_view()),
    ### Blogs and price indices
    path("Blogs/", views.ListBlogs.as_view()),
    path("Blog/<int:pk>", views.BlogDetails.as_view()),
    path("PriceIndex/", views.PriceIndex.as_view()),
    path("CityIndex/<int:pk>", views.CityIndex.as_view()),
    path("City/<int:pk>/", views.CitySpecificIndex.as_view()),
    path("Cities/", views.CityAllIndex.as_view()),
    ### Products
    path("Products/", views.Products.as_view()),
    path("Product/<int:pk>/", views.ProductDisplay.as_view()),
    path("CreateProduct/", views.CreateProduct.as_view()),
    path("DeleteProduct/<int:pk>/", views.DeleteProduct.as_view()),
    path("UpdateProduct/<int:pk>/", views.UpdateProduct.as_view()),
    ### Reviews
    path("Rating/<int:pk>/", views.RatingDisplay.as_view()),
    path("CreateRating/", views.CreateRating.as_view()),
    path("DeleteRating/<int:pk>/", views.DeleteReview.as_view()),
    ### Order and Order Items
    path("CreateOrder/", views.CreateOrder.as_view()),
    path("OrderDetails/<int:pk>/", views.OrderDetails.as_view()),
    path("CreateOrderItem/", views.CreateOrderItems.as_view()),
    path("Orders/", views.Orders.as_view()),
    path("CreateShipping/", views.CreateShipping.as_view()),
    path("ShippingDetails/<int:pk>/", views.ShippingDetails.as_view()),
    path("ShippingList/", views.Addresses.as_view()),
    path("DeleteShipping/<int:pk>/", views.DeleteAddress.as_view()),
    path('orders/', views.getOrders, name='orders'),
    path('orders/add/', views.addOrderItems, name='orders-add'),
    path('orders/myorders/', views.MyOrders.as_view(), name='myorders'),

    path('orders/<str:pk>/deliver/', views.updateOrderToDelivered, name='order-delivered'),

    path('orders/int:pk>/', views.OrderDetails.as_view(), name='user-order'),
    path('orders/<str:pk>/pay/', views.updateOrderToPaid, name='pay'),]
