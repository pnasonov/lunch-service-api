from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from restaurant.models import Restaurant
from restaurant.serializers import RestaurantSerializer


class RestaurantViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    # permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)
