from django.contrib import admin

from main.models import Product, Tag, Order, Customer

admin.site.register(Tag)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Customer)
