from django.urls import path, include
from rest_framework.routers import DefaultRouter

app_name = "v1"

urlpatterns = [
    path("basic/", include("basicinfo.api.v1.urls", namespace="basic")),
    path("instruments/", include("instruments.api.v1.urls", namespace="instruments")),
    path("logs/", include("logs.api.v1.urls", namespace="logs")),
]
