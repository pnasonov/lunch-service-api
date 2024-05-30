from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from django.utils.timezone import now

from restaurant.models import Restaurant, Menu
from restaurant.serializers import (
    RestaurantSerializer,
    RestaurantDetailSerializer,
    MenuSerializer,
)


class MenuViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class RestaurantViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    # permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)

    def get_queryset(self):
        if self.action == "retrieve":
            queryset = self.queryset.filter(menu__date_upload=now().date())
            return queryset

        return self.queryset

    def get_serializer_class(self):
        if self.action == "retrieve":
            return RestaurantDetailSerializer

        return RestaurantSerializer
