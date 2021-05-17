from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ["id", "email", "username", "password", "password2"]
        extra_kwargs = {"password": {"write_only": True}}

    def save(self):
        profile = User(
            email=self.validated_data["email"],
            username=self.validated_data["username"],
        )
        password = self._validated_data["password"]
        password2 = self.validated_data["password2"]
        if password != password2:
            raise serializers.ValidationError("passwords must match")
        profile.set_password(password)
        profile.save()
        return profile

    def validate(self, data):
        # check pwd is valid and hash it before saving
        if data.get('password'):
            if data['password'] != data.get('password2'):
                raise serializers.ValidationError('Passwords must match')

            del data['password2']
            data['password'] = make_password(data['password'])

        return data


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=128)
    password = serializers.CharField(max_length=128)
