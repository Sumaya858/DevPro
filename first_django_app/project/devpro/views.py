from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import RetrieveAPIView


from .models import Items
from .models import Order
from .models import Product
from .models import Whishlist
from .models import OrderProduct

from .serializers import ItemsSerializer
from .serializers import WhishlistSerializer
from .serializers import OrderProductSerializer
from .serializers import ProductSerializer
from .serializers import OrderSerializer


from rest_framework.authentication import TokenAuthentication
# Create your views here.


class ItemsListCreate(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer


class ItemsCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]    
    authentication_classes = [TokenAuthentication]

class ItemsDeleteView(DestroyAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer


class ItemsUpdateView(UpdateAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer


class ItemsRetrieveView(RetrieveAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer


class WishlistListCreate(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Whishlist.objects.all()
    serializer_class = WhishlistSerializer


class WhishlistCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]    
    authentication_classes = [TokenAuthentication]

class WhishlistDeleteView(DestroyAPIView):
    queryset = Whishlist.objects.all()
    serializer_class = WhishlistSerializer


class WhishlistUpdateView(UpdateAPIView):
    queryset = Whishlist.objects.all()
    serializer_class = WhishlistSerializer


class WhishlistRetrieveView(RetrieveAPIView):
    queryset = Whishlist.objects.all()
    serializer_class = WhishlistSerializer    


class OrderProductListCreate(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer


class OrderProductCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]    
    authentication_classes = [TokenAuthentication]

class OrderProductDeleteView(DestroyAPIView):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer

class OrderProductUpdateView(UpdateAPIView):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer


class OrderProductRetrieveView(RetrieveAPIView):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer        


class OrderListCreate(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]    
    authentication_classes = [TokenAuthentication]

class OrderDeleteView(DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderUpdateView(UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderRetrieveView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer  





class ProductListCreate(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]    
    authentication_classes = [TokenAuthentication]

class ProductDeleteView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductUpdateView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer               

