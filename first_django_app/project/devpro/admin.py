from django.contrib import admin
from .models import Items
from .models import Whishlist
from .models import OrderProduct
from .models import Order
from .models import Product
# Register your models here.


admin.site.register(Items)
admin.site.register(Whishlist)
admin.site.register(OrderProduct)
admin.site.register(Order)
admin.site.register(Product)