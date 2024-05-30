from rest_framework import routers

from restaurant.views import (
    RestaurantViewSet,
)

router = routers.DefaultRouter()
router.register("", RestaurantViewSet)

urlpatterns = router.urls

app_name = "restaurant"
