from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import filters

from django_filters.rest_framework import DjangoFilterBackend

from ...models import Network, Station
from logs.models import ManageLog, Record, LocationRecordItem
from .serializers import (
    NetworkSerializer,
    StationSerializer,
    StationCreatebyNetworkSerializer,
    StationCurrentDetailSerializer,
    StationSelectionSerializer,
)
from logs.api.v1.serializers import (
    ManageLogSerializer,
    RecordSerializer,
    LocationRecordItemSerializer,
)


class NetworkViewSet(viewsets.ModelViewSet):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer


class StationViewSet(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["network", "status"]
    search_fields = ["network__code", "code", "name"]


class StationSelectionView(generics.CreateAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSelectionSerializer

    def create(self, validated_data):
        ManageLogSerializer
        return super().create(self, validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

