from rest_framework import serializers

from restaurant.models import Restaurant, Menu, Employee


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ("id", "name", "surname", "position")


class MenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Menu
        fields = ("id", "date_upload", "restaurant", "description")


class MenuVotingSerializer(serializers.ModelSerializer):
    restaurant = serializers.SlugRelatedField(
        slug_field="name",
        read_only=True,
    )
    num_votes = serializers.IntegerField(read_only=True)

    class Meta:
        model = Menu
        fields = ("restaurant", "num_votes")


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
