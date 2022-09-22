from rest_framework import serializers
from .models import *


class SoilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soil
        fields = ['id', 'name', 'wilaya_id', 'created_by', 'created_at']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soil
        fields = ['id', 'name', 'wilaya_id', 'created_by', 'created_at']


class DeseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soil
        fields = ['id', 'name', 'wilaya_id', 'created_by', 'created_at']


