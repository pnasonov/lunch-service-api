from django.contrib import admin

from restaurant.models import Restaurant, Menu, Employee

admin.site.register(Restaurant)
admin.site.register(Menu)
admin.site.register(Employee)
