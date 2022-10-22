from rest_framework import serializers
from .models import *
class merchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = known_vendors
        fields = ['merchant_name', 'place']