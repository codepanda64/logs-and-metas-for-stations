from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

from . import views

app_name = "logs"

router = SimpleRouter()
router.register(r"manage-log", views.ManageLogViewSet)
router.register(r"before-status-check", views.BeforeStatusCheckViewSet)
router.register(r"after-status-check", views.ＡfterStatusCheckViewSet)


urlpatterns = []

urlpatterns += router.urls
