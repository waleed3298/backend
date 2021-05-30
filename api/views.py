from django.shortcuts import render
from rest_framework import generics, permissions, status, viewsets
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
import pickle
from django.http import HttpResponse, JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from datetime import datetime

from .models import (
    Ad,
    Saved,
    Blog,
    PriceIndex,
    YearlyIndices,
    Product,
    Indices,
    Review,
    Order,
    OrderItem,
    ShippingAddress,
    Profile,
)
from .serializers import (
    AdSerializer,
    UserSerializer,
    AdDetailSerializer,
    SavedSerializer,
    BlogSerializer,
    PriceIndexSerializer,
    YearlySerializer,
    ProductSerializer,
    RatingSerializer,
    IndicesSerializer,
    OrderSerializer,
    OrderItemSerializer,
    ShippingSerializer,
    ProfileSerializer,
)
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
import json
from rest_framework.views import APIView
from walkscore import WalkScoreAPI

### Walkscore API
class GetWalkscore(APIView):
    def post(self, request):
        api_key = "ffd1c56f9abcf84872116b4cc2dfcf31"
        walkscore_api = WalkScoreAPI(api_key=api_key)
        data = request.data
        address = "New York City, USA"
        result = walkscore_api.get_walk_score(
            latitude=37.0902, longitude=95.7129, address=address
        )
        score = result.walk_score
        print(result.transit_score)
        print(result.bike_score)
        return HttpResponse(result, score)


### Prediction Model
class predictions(APIView):
    def post(self, request):
        data = request.data
        if data["City"].lower() == "islamabad":
            Islamabad = "1"
            Karachi = "0"
            Lahore = "0"
            Rawalpindi = "0"
        elif data["City"].lower() == "lahore":
            Islamabad = "0"
            Karachi = "0"
            Lahore = "1"
            Rawalpindi = "0"
        elif data["City"].lower() == "karachi":
            Islamabad = "0"
            Karachi = "1"
            Lahore = "0"
            Rawalpindi = "0"
        elif data["City"].lower() == "rawalpindi":
            Islamabad = "0"
            Karachi = "0"
            Lahore = "0"
            Rawalpindi = "1"
        else:
            Islamabad = "0"
            Karachi = "0"
            Lahore = "0"
            Rawalpindi = "0"

        if data["Units"].lower() == "marla":
            Size = data["Size"]
            Marla = "1"
        else:
            Size = float(data["Size"]) * 20
            Marla = "0"

        if data["Type"].lower() == "house":
            House = 1
            Lower_Portion = 0
            Room = 0
            Upper_Portion = 0
            commercial_area = 0
            plot = 0
        elif data["Type"].lower() == "commercial_area":
            House = 0
            Lower_Portion = 0
            Room = 0
            Upper_Portion = 0
            commercial_area = 1
            plot = 0
        elif data["Type"].lower() == "plot":
            House = 0
            Lower_Portion = 0
            Room = 0
            Upper_Portion = 0
            commercial_area = 0
            plot = 1
        else:
            House = 0
            Lower_Portion = 0
            Room = 0
            Upper_Portion = 0
            commercial_area = 0
            plot = 0

        test = [
            [
                data["latitude"],
                data["longitude"],
                data["baths"],
                data["beds"],
                Size,
                Islamabad,
                Karachi,
                Lahore,
                Rawalpindi,
                House,
                Lower_Portion,
                Room,
                Upper_Portion,
                commercial_area,
                plot,
                Marla,
                "1",
            ]
        ]
        filename = "api/Saved_models/new_model.sav"
        loaded_model = pickle.load(open(filename, "rb"))
        result = loaded_model.predict(test)[0]
        return HttpResponse(int(result))


### USER VIEWS###
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserInfo(generics.ListAPIView):
    serializer_class = UserSerializer
    authentication_classes = [
        TokenAuthentication,
    ]

    def get_queryset(self):
        return User.objects.filter(email=self.request.user.email)


class GetUser(generics.ListAPIView):
    serializer_class = UserSerializer
    authentication_classes = [
        TokenAuthentication,
    ]
    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self):
        return User.objects.filter(email=self.request.user.email)


### ADVERTISEMENT VIEWS ###
class PropertyDisplay(generics.ListAPIView):
    queryset = Ad.objects.filter(Type="property")
    serializer_class = AdSerializer


class AdvertisementDisplay(generics.ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        "Location",
        "City",
        "Price",
        "Type",
        "Beds",
        "Baths",
        "Construction_status",
        "Purpose",
        "Units",
    ]


class SearchAds(generics.ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = (
        "@Location",
        "@User__username",
        "@City",
        "@Size",
        "@Units",
        "@Price",
        "@Purpose",
        "@Type",
        "@Construction_status",
        "@Beds",
        "@Baths",
    )


class PlotDisplay(generics.ListAPIView):
    queryset = Ad.objects.filter(Type="plot")
    serializer_class = AdSerializer


class CommercialDisplay(generics.ListAPIView):
    queryset = Ad.objects.filter(Type="commercial")
    serializer_class = AdSerializer


class Dashboard(generics.ListAPIView):
    serializer_class = AdSerializer
    authentication_classes = [
        TokenAuthentication,
    ]
    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self):
        return Ad.objects.filter(User=self.request.user)


class Recent(generics.ListAPIView):
    serializer_class = AdSerializer
    authentication_classes = [
        TokenAuthentication,
    ]
    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self):
        return Ad.objects.filter(User=self.request.user).order_by("id")[:4]


class CreateAd(generics.CreateAPIView):
    serializer_class = AdSerializer
    authentication_classes = [
        TokenAuthentication,
    ]
    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self):
        return Ad.objects.all(user="1")

    def perform_create(self, serializer):
        serializer.save(User=self.request.user)
        return JsonResponse(
            {"response": "Advertisement Created Successfully"}, status=201
        )


class AdDisplay(generics.RetrieveAPIView):
    serializer_class = AdDetailSerializer

    def get_queryset(self):
        pk = self.kwargs["pk"]
        return Ad.objects.filter(id=pk)


class DeleteAd(generics.RetrieveDestroyAPIView):
    serializer_class = AdSerializer

    def get_queryset(self):
        pk = self.kwargs["pk"]
        return Ad.objects.filter(id=pk)

    def perform_delete(self, serializer):
        serializer.delete()


class EditAd(generics.RetrieveUpdateAPIView):
    serializer_class = AdSerializer

    def get_queryset(self):
        pk = self.kwargs["pk"]
        return Ad.objects.filter(id=pk)


### LIKE UNLIKE VIEWS
class CreateLike(generics.CreateAPIView):
    serializer_class = SavedSerializer
    authentication_classes = [
        TokenAuthentication,
    ]
    permission_classes = [
        IsAuthenticated,
    ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return JsonResponse(
            {"response": "Advertisement Liked Successfully"}, status=201
        )


class LikedAds(generics.ListAPIView):
    serializer_class = SavedSerializer
    authentication_classes = [
        TokenAuthentication,
    ]
    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self):
        return Saved.objects.filter(user=self.request.user)


class DeleteLiked(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SavedSerializer

    def get_queryset(self):
        pk = self.kwargs["pk"]
        return Saved.objects.filter(id=pk)

    def perform_delete(self, serializer):
        serializer.delete()


class Liked(generics.RetrieveAPIView):
    serializer_class = SavedSerializer
    authentication_classes = [
        TokenAuthentication,
    ]
    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self):
        pk = self.kwargs["pk"]
        return Saved.objects.filter(Ad=pk, user=self.request.user)


class LatestAds(generics.ListAPIView):
    serializer_class = AdSerializer
    queryset = Ad.objects.all().order_by("-Time")[:6]


class MostViewed(generics.ListAPIView):
    serializer_class = AdSerializer
    queryset = Ad.objects.all().order_by("Views")[:6]


class Featured(generics.ListAPIView):
    serializer_class = AdSerializer
    queryset = Ad.objects.filter(Featured=True).order_by("id")[:6]


class ListBlogs(generics.ListAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()


class BlogDetails(generics.RetrieveAPIView):
    serializer_class = BlogSerializer

    def get_queryset(self):
        pk = self.kwargs["pk"]
        return Blog.objects.filter(id=pk)


class PriceIndex(generics.ListAPIView):
    serializer_class = PriceIndexSerializer
    queryset = PriceIndex.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["City"]


class Indices(generics.ListAPIView):
    serializer_class = IndicesSerializer
    queryset = Indices.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["City"]


class CityIndex(generics.RetrieveAPIView):
    serializer_class = PriceIndexSerializer

    def get_queryset(self):
        pk = self.kwargs["pk"]
        return PriceIndex.objects.filter(id=pk)


class CitySpecificIndex(generics.RetrieveAPIView):
    serializer_class = YearlySerializer

    def get_queryset(self):
        pk = self.kwargs["pk"]
        return YearlyIndices.objects.filter(id=pk)


class CityAllIndex(generics.ListAPIView):
    serializer_class = YearlySerializer
    queryset = YearlyIndices.objects.all()


class CreateProduct(generics.CreateAPIView):
    serializer_class = ProductSerializer
    authentication_classes = [
        TokenAuthentication,
    ]
    permission_classes = [
        IsAuthenticated,
    ]

    def perform_create(self, serializer):
        serializer.save(User=self.request.user)
        return JsonResponse({"response": "Product Saved Successfully"}, status=201)


class Products(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDisplay(generics.RetrieveAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        pk = self.kwargs["pk"]
        return Product.objects.filter(_id=pk)
        return Review.objects.filter(Product=pk)


class DeleteProduct(generics.RetrieveDestroyAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        pk = self.kwargs["pk"]
        return Product.objects.filter(_id=pk)

    def perform_delete(self, serializer):
        serializer.delete()


class UpdateProduct(generics.RetrieveUpdateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        pk = self.kwargs["pk"]
        return Ad.objects.filter(id=pk)


### RATING VIEWS
class RatingDisplay(generics.ListAPIView):
    serializer_class = RatingSerializer

    def get_queryset(self):
        pk = self.kwargs["pk"]
        return Review.objects.filter(Product=pk)


class CreateRating(generics.CreateAPIView):
    serializer_class = RatingSerializer
    authentication_classes = [
        TokenAuthentication,
    ]
    permission_classes = [
        IsAuthenticated,
    ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return JsonResponse({"response": "Review Saved Successfully"}, status=201)


class DeleteReview(generics.RetrieveDestroyAPIView):
    serializer_class = RatingSerializer

    def get_queryset(self):
        pk = self.kwargs["pk"]
        return Review.objects.filter(_id=pk)

    def perform_delete(self, serializer):
        if serializer.user == self.request.user:
            serializer.delete()
        else:
            return JsonResponse(
                {"error": "Only users can delete their own review"}, status=201
            )


### ORDER AND SHIPPING ADDRESS
class CreateOrder(generics.CreateAPIView):
    serializer_class = OrderSerializer
    authentication_classes = [
        TokenAuthentication,
    ]
    permission_classes = [
        IsAuthenticated,
    ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return JsonResponse({"response": "Order Saved Successfully"}, status=201)


class OrderDetails(generics.RetrieveAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        pk = self.kwargs["pk"]
        return Order.objects.filter(_id=pk)


class Orders(generics.ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class UpdateOrder(generics.RetrieveUpdateAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        pk = self.kwargs["pk"]
        return Order.objects.filter(_id=pk)


class CreateOrderItems(generics.CreateAPIView):
    serializer_class = OrderItemSerializer
    authentication_classes = [
        TokenAuthentication,
    ]
    permission_classes = [
        IsAuthenticated,
    ]

    def perform_create(self, serializer):
        serializer.save()
        return JsonResponse({"response": "Order Item Saved Successfully"}, status=201)


class CreateShipping(generics.CreateAPIView):
    serializer_class = ShippingSerializer
    authentication_classes = [
        TokenAuthentication,
    ]
    permission_classes = [
        IsAuthenticated,
    ]

    def perform_create(self, serializer):
        serializer.save()
        return JsonResponse({"response": "Address Saved Successfully"}, status=201)


class ShippingDetails(generics.RetrieveAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        pk = self.kwargs["pk"]
        return ShippingAddress.objects.filter(Order=pk)


class Addresses(generics.ListAPIView):
    serializer_class = OrderSerializer
    queryset = ShippingAddress.objects.all()


class DeleteAddress(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ShippingSerializer

    def get_queryset(self):
        pk = self.kwargs["pk"]
        return ShippingAddress.objects.filter(_id=pk)

    def perform_delete(self, serializer):
        serializer.delete()


@api_view(["POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def addOrderItems(request):
    user = request.user
    data = request.data

    orderItems = data["orderItems"]

    if orderItems and len(orderItems) == 0:
        return Response(
            {"detail": "No Order Items"}, status=status.HTTP_400_BAD_REQUEST
        )
    else:

        # (1) Create order
        if (data["isPaid"]) == "true":
            isPaid = True
        else:
            isPaid = False
        order = Order.objects.create(
            user=user,
            paymentMethod=data["paymentMethod"],
            isPaid=isPaid,
            taxPrice=data["taxPrice"],
            shippingPrice=data["shippingPrice"],
            totalPrice=data["totalPrice"],
        )

        # (2) Create shipping address

        shipping = ShippingAddress.objects.create(
            order=order,
            address=data["shippingAddress"]["address"],
            city=data["shippingAddress"]["city"],
            postalCode=data["shippingAddress"]["postalCode"],
            country=data["shippingAddress"]["country"],
        )

        # (3) Create order items adn set order to orderItem relationship
        for i in orderItems:
            product = Product.objects.get(_id=i["product"])

            item = OrderItem.objects.create(
                product=product,
                order=order,
                name=product.name,
                qty=i["qty"],
                price=i["price"],
                image=product.image.url,
            )

            # (4) Update stock

            product.countInStock -= item.qty
            product.save()

        serializer = OrderSerializer(order, many=False)
        return Response(serializer.data)


class MyOrders(generics.ListAPIView):
    serializer_class = OrderSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def getOrders(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def updateOrderToPaid(request, pk):
    order = Order.objects.get(_id=pk)

    order.isPaid = True
    order.paidAt = datetime.now()
    order.save()

    return Response("Order was paid")


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def updateOrderToDelivered(request, pk):
    order = Order.objects.get(_id=pk)

    order.isDelivered = True
    order.deliveredAt = datetime.now()
    order.save()

    return Response("Order was delivered")


### Profile Management
class CreateProfile(generics.CreateAPIView):
    serializer_class = ProfileSerializer
    authentication_classes = [
        TokenAuthentication,
    ]
    permission_classes = [
        IsAuthenticated,
    ]

    def perform_create(self, serializer):
        serializer.save(User=self.request.user)
        return JsonResponse({"response": "Profile Saved Successfully"}, status=201)


class MyProfile(generics.ListAPIView):
    serializer_class = ProfileSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Profile.objects.filter(User=self.request.user)


class UpdateProfile(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer

    def get_queryset(self):
        pk = self.kwargs["pk"]
        return Profile.objects.filter(id=pk)


class GetProfile(generics.RetrieveAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        pk = self.kwargs["pk"]
        return User.objects.filter(id=pk)


class Profiles(generics.ListAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class ProductSearch(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["name", "brand", "price", "category"]
