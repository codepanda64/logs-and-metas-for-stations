from django.core.management.base import BaseCommand

from basicinfo.models import Network, Station


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "stations_file", type=str, help="The file that contains the stations info"
        )

    def handle(self, *args, **kwargs):
        stations_file = kwargs["stations_file"]
        with open(f"{stations_file}.txt") as file:
            for line in file:
                line = line.strip("\n")
                net, code, name, latitude, longitude, altitude = line.split(",")
                Network.objects.get_or_create(code=net, slug=str.lower(net))
                latitude = 0.0 if latitude == "" else latitude
                longitude = 0.0 if longitude == "" else longitude
                altitude = 0.0 if altitude == "" else altitude

                network = Network.objects.get(code=net)
                station = Station(
                    net=network,
                    code=code,
                    name=name,
                    slug=str.lower(f"{network.code}-{code}"),
                    latitude=latitude,
                    longitude=longitude,
                    altitude=altitude,
                )

                station.save()

        self.stdout.write(self.style.SUCCESS("Stations imported successfully!"))
