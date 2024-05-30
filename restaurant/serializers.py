from rest_framework import serializers

from restaurant.models import Restaurant, Menu


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ("id", "date_upload", "restaurant", "description")


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ("id", "name", "description")


class RestaurantDetailSerializer(RestaurantSerializer):
    menu = MenuSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Restaurant
        fields = ("id", "name", "menu")
