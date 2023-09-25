from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import RetrieveAPIView

from .models import Whishlist
from .serializers import ItemsSerializer
from .serializers import WhishlistSerializer

from .models import Items
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

