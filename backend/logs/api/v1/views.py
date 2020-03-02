from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from rest_framework import filters

import django_filters

# from django_filters import DateFilter,

# from django_filters.rest_framework import FilterSet
from django_filters.rest_framework import DjangoFilterBackend

from ...models import (
    ManageLog,
    BeforeStatusCheck,
    AfterStatusCheck,
    Record,
    LocationRecordItem,
    InstrumentEntityRecordItem,
    CommmonInstrumentRecordItem,
    InsertDiskRecordItem,
    CollectedDataRecordItem,
)
from .serializers import (
    ManageLogSerializer,
    BeforeStatusCheckSerializer,
    AfterStatusCheckSerializer,
    RecordSerializer,
    LocationRecordItemSerializer,
    InstrumentEntityRecordItemSerializer,
    CommmonInstrumentRecordItemSerializer,
    InsertDiskRecordItemSerializer,
    CollectedDataRecordItemSerializer,
)


class ManageLogFilter(django_filters.FilterSet):
    """
    为ManageLog添加过滤条件
    台站编号：station=station_id
    管理年份：managed_date__year=year
    before_state: True|False
    after_state: True|False
    """

    class Meta:
        model = ManageLog
        fields = {
            "station": ["exact"],
            "managed_date": ["exact", "year"],
            "before_state": ["exact"],
            "after_state": ["exact"],
        }


class ManageLogViewSet(viewsets.ModelViewSet):
    queryset = ManageLog.objects.all()
    serializer_class = ManageLogSerializer
    filter_class = ManageLogFilter


class BeforeStatusCheckViewSet(viewsets.ModelViewSet):
    queryset = BeforeStatusCheck.objects.all()
    serializer_class = BeforeStatusCheckSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["manage_log"]


class AfterStatusCheckViewSet(viewsets.ModelViewSet):
    queryset = AfterStatusCheck.objects.all()
    serializer_class = BeforeStatusCheckSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["manage_log"]


class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer


class LocationRecordItemViewSet(viewsets.ModelViewSet):
    queryset = LocationRecordItem.objects.all()
    serializer_class = LocationRecordItemSerializer


class InstrumentEntityRecordItemViewSet(viewsets.ModelViewSet):
    queryset = InstrumentEntityRecordItem.objects.all()
    serializer_class = InstrumentEntityRecordItemSerializer


class CommmonInstrumentRecordItemViewSet(viewsets.ModelViewSet):
    queryset = CommmonInstrumentRecordItem.objects.all()
    serializer_class = CommmonInstrumentRecordItemSerializer


class InsertDiskRecordItemViewSet(viewsets.ModelViewSet):
    queryset = InsertDiskRecordItem.objects.all()
    serializer_class = InsertDiskRecordItemSerializer


class CollectedDataRecordItemViewSet(viewsets.ModelViewSet):
    queryset = CollectedDataRecordItem.objects.all()
    serializer_class = CollectedDataRecordItemSerializer
