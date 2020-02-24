from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from ...models import (
    ManageLog,
    BeforeStatusCheck,
    AfterStatusCheck,
    Record,
    LocationRecord,
    InstrumentEntityRecord,
    CommmonInstrumentRecord,
    InsertDiskRecord,
    CollectedDataRecord,
)
from .serializers import (
    ManageLogSerializer,
    BeforeStatusCheckSerializer,
    AfterStatusCheckSerializer,
    RecordSerializer,
    LocationRecordSerializer,
    InstrumentEntityRecordSerializer,
    CommmonInstrumentRecordSerializer,
    InsertDiskRecordSerializer,
    CollectedDataRecordSerializer,
)


class ManageLogViewSet(viewsets.ModelViewSet):
    queryset = ManageLog.objects.all()
    serializer_class = ManageLogSerializer


class BeforeStatusCheckViewSet(viewsets.ModelViewSet):
    queryset = BeforeStatusCheck.objects.all()
    serializer_class = BeforeStatusCheckSerializer


class AfterStatusCheckViewSet(viewsets.ModelViewSet):
    queryset = AfterStatusCheck.objects.all()
    serializer_class = BeforeStatusCheckSerializer
