from rest_framework import serializers
from .models import Items
from .models import Whishlist
from .models import Order
from .models import Product
from .models import OrderProduct


class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = '__all__'


class WhishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Whishlist
        fields = '__all__'   

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = '__all__'



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'                             