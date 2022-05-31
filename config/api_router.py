from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from backend.users.api.views import UserViewSet, LentsViewSet
from backend.vehicles.api.views.vehicles import VehicleViewSet
from backend.vehicles.api.views.workdays import VehicleWorkDayViewSet, ExpensesVehicleWorkdayViewSet
from backend.services.api.views import ReadFieldsViewset, ExpedienteViewset

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("vehicles", VehicleViewSet)
router.register("vehicles-workday", VehicleWorkDayViewSet)
router.register("lents", LentsViewSet)
router.register("expenses", ExpensesVehicleWorkdayViewSet)
router.register(r"data-for-services", ReadFieldsViewset, basename='services.models.Expediente')
router.register(r"expedientes", ExpedienteViewset, basename='services.models.Expediente')


app_name = "api"
urlpatterns = router.urls
