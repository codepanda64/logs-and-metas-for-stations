from rest_framework import serializers

# from rest_framework.reverse import reverse

from ...models import Network, Station, StationMoreInfo


class NetworkSerializer(serializers.ModelSerializer):
    # stations = serializers.HyperlinkedRelatedField(
    #     many=True, view_name="station_detail", read_only=True
    # )

    class Meta:
        model = Network
        fields = "__all__"
        # fields = (
        #     "code",
        #     "url",
        #     "name",
        #     "created",
        #     "updated",
        #     "remark",
        # )


# class StationHyperlinkedIdentityField(serializers.HyperlinkedIdentityField):

#     def get_url(self, obj, view_name, request, format):
#         print("get_url")
#         url_kwargs = {"network_id": obj.network.id, "pk": obj.pk}
#         return self.reverse(
#             view_name, kwargs=url_kwargs, request=request, format=format
#         )

#     def get_object(self, view_name, view_args, view_kwargs):
#         lookup_kwargs = {
#             "network__id": view_kwargs["network_id"],
#             "pk": view_kwargs["pk"],
#         }
#         return self.get_queryset().get(**lookup_kwargs)


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = (
            "id",
            "network",
            "code",
            "name",
            "latitude",
            "longitude",
            "altitude",
            "status",
        )


class StationCreatebyNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = (
            "id",
            "code",
            "name",
            "latitude",
            "longitude",
            "altitude",
            "status",
        )


class StationCurrentDetailSerializer(serializers.ModelSerializer):
    establish = serializers.DateTimeField(read_only=True)
    removal = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Station
        fields = (
            "network",
            "code",
            "name",
            "latitude",
            "longitude",
            "altitude",
            "status",
            "establish",
            "removal"
            # "seismic_instruments",
        )


class StationMoreInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StationMoreInfo
        fields = ("geo_desciription", "lithology_description", "other_info")


class StationSelectionSerializer(serializers.ModelSerializer):
    """
    台站勘选基本信息
    """

    more_info = StationMoreInfoSerializer()

    class Meta:
        model = Station
        fields = (
            "network",
            "code",
            "name",
            "latitude",
            "longitude",
            "altitude",
            "selection",
            "status",
            "more_info",
        )

    def create(self, validated_data):
        more_info = validated_data.pop("more_info")
        station = Station.objects.create(**validated_data)
        StationMoreInfo.objects.create(station=station, **more_info)
        return station
