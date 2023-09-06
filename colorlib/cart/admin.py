from django.contrib import admin

# Register your models here.
from cart.models import Cart
admin.site.register(Cart)
from cart.models import Order
admin.site.register(Order)
from cart.models import Account
admin.site.register(Account)