from django.urls import path
from .views import ItemsListCreate
from .views import ItemsCreateView
from .views import ItemsListView
from .views import ItemsDeleteView
from .views import ItemsUpdateView
from .views import ItemsRetrieveView

from .views import WhishlistListCreate
from .views import WhishlistCreateView
from .views import WhishlistListView
from .views import WhishlistDeleteView
from .views import WhishlistUpdateView
from .views import WhishlistRetrieveView


urlpatterns = [
    path('api/items/', ItemsListCreate.as_view()),
    path('api/items/create/', ItemsCreateView()),
    path('api/items/list/',ItemsListView.as_view()),
    path('api/items/<pk>/delete', ItemsDeleteView.as_view()),
    path('api/items/<pk>/update', ItemsUpdateView.as_view()),
    path('api/items/<pk>/retrieve', ItemsRetrieveView.as_view()),

    path('api/whishlist/', WhishlistListCreate.as_view()),
    path('api/whishlist/create/', WhishlistCreateView()),
    path('api/whishlist/list/',WhishlistListView.as_view()),
    path('api/whishlist/<pk>/delete', WhishlistDeleteView.as_view()),
    path('api/whishlist/<pk>/update', WhishlistUpdateView.as_view()),
    path('api/whishlist/<pk>/retrieve', WhishlistRetrieveView.as_view()),

]
