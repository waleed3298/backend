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
    ### Profile Management
    path("CreateProfile/", views.CreateProfile.as_view()),
    path("UpdateProfile/<str:pk>/", views.UpdateProfile.as_view()),
    path("myProfile/", views.MyProfile.as_view()),
    ### Property Management
    path("properties/", views.PropertyDisplay.as_view()),  # GET Method
    path("plots/", views.PlotDisplay.as_view()),  # GET Method
    path("commercial/", views.CommercialDisplay.as_view()),  # GET Method
    path(
        "CreateAd/", views.CreateAd.as_view()
    ),  # POST Method, Headers->Token, Body->Data
    path("AD/<int:pk>/", views.AdDisplay.as_view()),  # GET Method
    path("Delete/<int:pk>/", views.DeleteAd.as_view()),  # DELETE Method, Headers->Token
    path("Edit/<int:pk>/", views.EditAd.as_view()),  # PUT Method
    path("advertisements/", views.AdvertisementDisplay.as_view()),  # GET Method
    path("searchAds/", views.SearchAds.as_view()),
    path("dashboard/", views.Dashboard.as_view()),
    path("recent/", views.Recent.as_view()),
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
    path("Products/", views.Products.as_view()),  # GET Method for list of all products
    path(
        "Product/<int:pk>/", views.ProductDisplay.as_view()
    ),  # GET Method for a specific product
    path(
        "CreateProduct/", views.CreateProduct.as_view()
    ),  # POST Method for creating new product
    path(
        "DeleteProduct/<int:pk>/", views.DeleteProduct.as_view()
    ),  # DELETE Method for deleting
    path(
        "UpdateProduct/<int:pk>/", views.UpdateProduct.as_view()
    ),  # PUT Method for updating
    ### Reviews
    path("Rating/<int:pk>/", views.RatingDisplay.as_view()),  # GET Method for ratings
    path(
        "CreateRating/", views.CreateRating.as_view()
    ),  # POST Method for creating new rating
    path(
        "DeleteRating/<int:pk>/", views.DeleteReview.as_view()
    ),  # POST Method for deleting rating
    ### Order and Order Items
    path("CreateOrder/", views.CreateOrder.as_view()),
    path("OrderDetails/<int:pk>/", views.OrderDetails.as_view()),
    path("CreateOrderItem/", views.CreateOrderItems.as_view()),
    path("Orders/", views.Orders.as_view()),
    path(
        "CreateShipping/", views.CreateShipping.as_view()
    ),  # POST Method for creating shipping
    path("ShippingDetails/<int:pk>/", views.ShippingDetails.as_view()),
    path("ShippingList/", views.Addresses.as_view()),
    path("DeleteShipping/<int:pk>/", views.DeleteAddress.as_view()),
    path("orders/", views.getOrders, name="orders"),  # GET Method for list of orders
    path(
        "orders/add/", views.addOrderItems, name="orders-add"
    ),  # POST Method for creating order
    path(
        "orders/myorders/", views.MyOrders.as_view(), name="myorders"
    ),  # GET Method for getting my orders
    path(
        "orders/<str:pk>/deliver/", views.updateOrderToDelivered, name="order-delivered"
    ),
    path("orders/int:pk>/", views.OrderDetails.as_view(), name="user-order"),
    path("orders/<str:pk>/pay/", views.updateOrderToPaid, name="pay"),
    ### ML model
    path("model/", views.predictions.as_view()),
]
