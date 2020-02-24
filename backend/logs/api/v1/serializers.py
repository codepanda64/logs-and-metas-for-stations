from rest_framework import serializers

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


class ManageLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManageLog
        fields = "__all__"


class BeforeStatusCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeforeStatusCheck
        fields = "__all__"


class AfterStatusCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = AfterStatusCheck
        fields = "__all__"


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = "__all__"


class LocationRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationRecord
        fields = "__all__"


class InstrumentEntityRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstrumentEntityRecord
        fields = "__all__"


class CommmonInstrumentRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommmonInstrumentRecord
        fields = "__all__"


class InsertDiskRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsertDiskRecord
        fields = "__all__"


class CollectedDataRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectedDataRecord
        fields = "__all__"
