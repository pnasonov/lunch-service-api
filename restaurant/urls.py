from rest_framework import routers

from restaurant.views import RestaurantViewSet, MenuViewSet

router = routers.DefaultRouter()
router.register("restaurants", RestaurantViewSet)
router.register("menus", MenuViewSet)


urlpatterns = router.urls

app_name = "restaurant"
