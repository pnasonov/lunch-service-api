from django.db.models import Count
from rest_framework import mixins, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from django.utils.timezone import now

from restaurant.models import Restaurant, Menu, Employee
from restaurant.serializers import (
    RestaurantSerializer,
    RestaurantDetailSerializer,
    MenuSerializer,
    MenuVotingSerializer,
    EmployeeSerializer,
)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_voting_results(request: Request) -> Response:
    queryset = Menu.objects.filter(date_upload=now().date()).annotate(
        num_votes=Count("voters")
    )
    serializer = MenuVotingSerializer(queryset, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


class EmployeeViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    # permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)


class MenuViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = Menu.objects.select_related("restaurant").prefetch_related(
        "voters"
    )
    serializer_class = MenuSerializer
    # permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)


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
