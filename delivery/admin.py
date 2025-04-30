from django.contrib import admin

from .models import Customer,Restaurant
# Register your models here.
admin.site.register(Customer)
admin.site.register(Restaurant)