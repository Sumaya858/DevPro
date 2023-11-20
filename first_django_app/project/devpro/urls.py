from django.urls import path
from .views import ItemsListCreate
from .views import ItemsCreateView
from .views import ItemsListView
from .views import ItemsDeleteView
from .views import ItemsUpdateView
from .views import ItemsRetrieveView

from .views import WishlistListCreate
from .views import WhishlistCreateView
from .views import WhishlistListView
from .views import WhishlistDeleteView
from .views import WhishlistUpdateView
from .views import WhishlistRetrieveView

from .views import OrderProductListCreate
from .views import OrderProductCreateView
from .views import OrderProductListView
from .views import OrderProductDeleteView
from .views import OrderProductUpdateView
from .views import OrderProductRetrieveView

from .views import OrderListCreate
from .views import OrderCreateView
from .views import OrderListView
from .views import OrderDeleteView
from .views import OrderUpdateView
from .views import OrderRetrieveView

from .views import ProductListCreate
from .views import ProductCreateView
from .views import ProductListView
from .views import ProductDeleteView
from .views import ProductUpdateView
from .views import ProductRetrieveView


urlpatterns = [
    path('api/items/', ItemsListCreate.as_view()),
    path('api/items/create/', ItemsCreateView()),
    path('api/items/list/',ItemsListView.as_view()),
    path('api/items/<pk>/delete', ItemsDeleteView.as_view()),
    path('api/items/<pk>/update', ItemsUpdateView.as_view()),
    path('api/items/<pk>/retrieve', ItemsRetrieveView.as_view()),

    path('api/whishlist/', WishlistListCreate.as_view()),
    path('api/whishlist/create/', WhishlistCreateView()),
    path('api/whishlist/list/',WhishlistListView.as_view()),
    path('api/whishlist/<pk>/delete', WhishlistDeleteView.as_view()),
    path('api/whishlist/<pk>/update', WhishlistUpdateView.as_view()),
    path('api/whishlist/<pk>/retrieve', WhishlistRetrieveView.as_view()),


    path('api/orderproduct/', OrderProductListCreate.as_view()),
    path('api/orderproduct/create/', OrderProductCreateView()),
    path('api/orderproduct/list/',OrderProductListView.as_view()),
    path('api/orderproduct/<pk>/delete', OrderProductDeleteView.as_view()),
    path('api/orderproduct/<pk>/update', OrderProductUpdateView.as_view()),
    path('api/orderproduct/<pk>/retrieve', OrderProductRetrieveView.as_view()),

    path('api/order/', OrderListCreate.as_view()),
    path('api/order/create/', OrderCreateView()),
    path('api/order/list/',OrderListView.as_view()),
    path('api/order/<pk>/delete', OrderDeleteView.as_view()),
    path('api/order/<pk>/update', OrderUpdateView.as_view()),
    path('api/order/<pk>/retrieve', OrderRetrieveView.as_view()),

    path('api/product/', ProductListCreate.as_view()),
    path('api/product/create/', ProductCreateView()),
    path('api/product/list/',ProductListView.as_view()),
    path('api/product/<pk>/delete', ProductDeleteView.as_view()),
    path('api/product/<pk>/update', ProductUpdateView.as_view()),
    path('api/product/<pk>/retrieve', ProductRetrieveView.as_view()),

]
