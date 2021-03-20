from rest_framework import serializers
from .models import Ad,Saved,Product,OrderItem,Order,Review,ShippingAddress,PriceIndex,Blog,YearlyIndices
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model = User
        fields = ['id','email','username','password','password2']
        extra_kwargs = {
            'password': {'write_only':True}
        }
        
    def save(self):
        profile = User(
            email = self.validated_data['email'],
            username = self.validated_data['username'],
        )
        password = self._validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError('passwords must match')
        profile.set_password(password)
        profile.save()
        return profile

class AdSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ad
        fields = ['id','Title','Image','Description','Price','Size','Units','Beds','Baths','Construction_status','Image1','Image2','Image3','Image4','Image5','City','Location','Purpose','Type','latitude','longitude','Views','Featured','Time','contact_no','cell_no','email']


class SavedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saved
        fields = ['id','Ad','Title','Price']
           
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class ShippingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = '__all__'

class PriceIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceIndex
        fields = '__all__'
class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
class YearlySerializer(serializers.ModelSerializer):
    class Meta:
        model = YearlyIndices
        fields = '__all__'