from django.urls import path
from rest_framework import routers

from restaurant.views import (
    RestaurantViewSet,
    MenuViewSet,
    EmployeeViewSet,
    get_voting_results,
)

router = routers.DefaultRouter()
router.register("restaurants", RestaurantViewSet)
router.register("menus", MenuViewSet)
router.register("employees", EmployeeViewSet)


urlpatterns = [
    path("voting/", get_voting_results, name="voting"),
] + router.urls

app_name = "restaurant"
