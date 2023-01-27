from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    director = serializers.StringRelatedField()
    class Meta:
        model = Product
        fields = '__all__'

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'       