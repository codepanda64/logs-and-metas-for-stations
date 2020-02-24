from rest_framework import serializers

from ...models import Instrument, InstrumentEntity


class InstrumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instrument
        fields = "__all__"


class InstrumentEntitySerializer(serializers.ModelSerializer):
    # instrument_model = serializers.StringRelatedField()
    # Instrument_model = InstrumentSerializer()

    class Meta:
        model = InstrumentEntity
        fields = "__all__"
        # fields = ("id", "sn", "instrument_model", "belong")


class InstrumentEntityCreateSerializer(serializers.ModelSerializer):
    # instrument_model = serializers.StringRelatedField()

    class Meta:
        model = InstrumentEntity
        fields = ("id", "sn", "status", "belong")
