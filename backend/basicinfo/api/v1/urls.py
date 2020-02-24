from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

from . import views

app_name = "basic_info"

router = SimpleRouter()
router.register(r"networks", views.NetworkViewSet)
router.register(
    r"networks/(?P<network_id>[0-9]+)/stations",
    views.StationViewSet,
    basename="station-by-network",
)


urlpatterns = [
    path("stations/", views.StationListCreateView.as_view(), name="station-list",),
]

urlpatterns += router.urls
