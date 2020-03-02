from rest_framework import serializers

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


class LocationRecordItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationRecordItem
        fields = "__all__"


class InstrumentEntityRecordItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstrumentEntityRecordItem
        fields = "__all__"


class CommmonInstrumentRecordItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommmonInstrumentRecordItem
        fields = "__all__"


class InsertDiskRecordItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsertDiskRecordItem
        fields = "__all__"


class CollectedDataRecordItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectedDataRecordItem
        fields = "__all__"


class ManageLogDetailSerializer(serializers.ModelSerializer):
    records = RecordSerializer(many=True)

    class Meta:
        model = ManageLog
        fields = ("station", "managed_date", "records")

