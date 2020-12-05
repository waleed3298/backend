from rest_framework import serializers
from .models import Ad

class AdSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ad
        fields = ['id','Title','Image','Description','Price','Size','Units','Beds','Baths','Construction_status','City','Location','Purpose','Type','User']
