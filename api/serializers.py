from rest_framework import serializers
from .models import Ad,Profile,Saved
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)

    class Meta:
        model = User
        fields = ['email','username','password','password2']
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
        fields = ['id','Title','Image','Description','Price','Size','Units','Beds','Baths','Construction_status','Image1','Image2','Image3','Image4','Image5','City','Location','Purpose','Type','latitude','longitude','Views','Featured','Time']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['name','image','Age','contact_no']

class SavedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saved
        fields = ['id','Ad','Title','Price']