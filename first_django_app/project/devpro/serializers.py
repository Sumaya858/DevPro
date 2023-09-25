from rest_framework import serializers
from .models import Items
from .models import Whishlist


class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = '__all__'


class WhishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Whishlist
        fields = '__all__'        