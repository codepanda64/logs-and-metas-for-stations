from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

from . import views

app_name = "instruments"

router = SimpleRouter()
router.register(r"models", views.InstrumentModelViewSet)
router.register(
    r"models/(?P<instrument_model_id>[0-9]+)/entities", views.InstrumentEntityViewSet
)

urlpatterns = []

urlpatterns += router.urls

