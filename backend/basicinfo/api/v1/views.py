from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from ...models import Network, Station
from .serializers import (
    NetworkSerializer,
    StationSerializer,
    StationCreatebyNetworkSerializer,
    StationCurrentDetailSerializer,
    StationSelectionSerializer,
)


class NetworkViewSet(viewsets.ModelViewSet):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer


class StationViewSet(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer

    parent_lookup_field = "network_id"
    lookup_field = "pk"

    def get_serializer_class(self):
        if self.parent_lookup_field in self.kwargs.keys() and self.action == "create":
            return StationCreatebyNetworkSerializer
        return self.serializer_class

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.parent_lookup_field in self.kwargs.keys():
            queryset = queryset.filter(network_id=self.kwargs[self.parent_lookup_field])
        return queryset

    def get_object(self):
        queryset = self.get_queryset()
        filter = {}
        filter[self.lookup_field] = self.kwargs[self.lookup_field]

        obj = get_object_or_404(queryset, **filter)
        self.check_object_permissions(self.request, obj)
        return obj

    def perform_create(self, serializer):
        if self.parent_lookup_field in self.kwargs.keys():
            kwargs = {}
            kwargs[self.parent_lookup_field] = self.kwargs[self.parent_lookup_field]
            serializer.save(**kwargs)
        else:
            serializer.save()


class StationListCreateView(generics.ListCreateAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer


class StationSelectionView(generics.CreateAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSelectionSerializer

