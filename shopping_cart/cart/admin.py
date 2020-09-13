from django.contrib import admin
from .models import Product, Guest


# Register Product Model in admin site.
admin.site.register(Product)

# Register Guest Model in admin site.
admin.site.register(Guest)