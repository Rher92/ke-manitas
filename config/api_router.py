from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from backend.users.api.views import UserViewSet
from backend.vehicles.api.views.vehicles import VehicleViewSet
from backend.vehicles.api.views.workdays import VehicleWorkDayViewSet


if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("vehicles", VehicleViewSet)
router.register("vehicles-workday", VehicleWorkDayViewSet)

app_name = "api"
urlpatterns = router.urls
