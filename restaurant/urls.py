from rest_framework import routers

from restaurant.views import RestaurantViewSet, MenuViewSet, EmployeeViewSet

router = routers.DefaultRouter()
router.register("restaurants", RestaurantViewSet)
router.register("menus", MenuViewSet)
router.register("employees", EmployeeViewSet)


urlpatterns = router.urls

app_name = "restaurant"
