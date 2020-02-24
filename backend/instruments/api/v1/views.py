from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from ...models import Instrument, InstrumentEntity
from .serializers import (
    InstrumentSerializer,
    InstrumentEntitySerializer,
    InstrumentEntityCreateSerializer,
)


class InstrumentModelViewSet(viewsets.ModelViewSet):
    queryset = Instrument.objects.all()
    serializer_class = InstrumentSerializer


class InstrumentEntityViewSet(viewsets.ModelViewSet):
    queryset = InstrumentEntity.objects.all()
    serializer_class = InstrumentEntitySerializer
    serializer_action_classes = {
        "create": InstrumentEntityCreateSerializer,
    }
    parent_lookup_field = "instrument_model_id"
    lookup_field = "pk"

    def _allowed_methods(self):
        """
        uri: model/<int:instrument_model_id>/entities/
        查找`instrument_model_id` 如果其 `is_model` 为 False ， 将不允许操作
        """
        if self.parent_lookup_field in self.kwargs.keys():
            instrument = get_object_or_404(
                Instrument, id=self.kwargs[self.parent_lookup_field]
            )
            if not instrument.is_model:
                print("allowed_methods:none")
                return []
                # return [
                #     m
                #     for m in super()._allowed_methods()
                #     if m not in ["POST", "PUT", "PATCH", "DELETE"]
                # ]

        return super()._allowed_methods()

    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return self.serializer_class

    def get_queryset(self):
        queryset = super().get_queryset()
        filter = {}
        filter[self.parent_lookup_field] = self.kwargs[self.parent_lookup_field]
        queryset = queryset.filter(**filter)
        return queryset

    def get_object(self):
        queryset = self.get_queryset()
        print(queryset)
        filter = {}
        # for field in self.multiple_lookup_fields:
        # filter[field] = self.kwargs.get(field, None)
        filter[self.lookup_field] = self.kwargs[self.lookup_field]

        obj = get_object_or_404(queryset, **filter)
        self.check_object_permissions(self.request, obj)
        return obj

    def perform_create(self, serializer):
        if "instrument_model_id" in self.kwargs.keys():
            instrument = get_object_or_404(
                Instrument, id=self.kwargs["instrument_model_id"]
            )
            if instrument.is_model:
                serializer.save(instrument_model__id=self.kwargs["instrument_model_id"])


"""
class InstrumentEntityCreateView(generics.CreateAPIView):
    queryset = InstrumentEntity.objects.all()
    serializer_class = InstrumentEntityCreateSerializer

    multiple_lookup_fields = ("model_id", "pk")

    def post(self, request, *args, **kwargs):
        if "model_id" in self.kwargs.keys():
            instrument_model = get_object_or_404(Instrument, id=self.kwargs["model_id"])
            if not instrument_model.has_sn:
                return Response(status=status.HTTP_400_BAD_REQUEST)

        return super().post(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if "model_id" in self.kwargs.keys():
            queryset = queryset.filter(instrument_model__id=self.kwargs["model_id"])
        return queryset

    def perform_create(self, serializer):
        if "model_id" in self.kwargs.keys():
            instrument_model = get_object_or_404(Instrument, id=self.kwargs["model_id"])
            if instrument_model.has_sn:
                serializer.save(instrument_model__id=self.kwargs["model_id"])
            else:
                # Todo
                pass
        else:
            serializer.save()
"""


class InstrumentEntityDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InstrumentEntity.objects.all()
    serializer_class = InstrumentEntitySerializer
    multiple_lookup_fields = ("model_id", "pk")

    def get_object(self):
        queryset = self.get_queryset()
        filter = {}
        for field in self.multiple_lookup_fields:
            filter[field] = self.kwargs[field]

        obj = get_object_or_404(queryset, **filter)
        self.check_object_permissions(self.request, obj)
        return obj
