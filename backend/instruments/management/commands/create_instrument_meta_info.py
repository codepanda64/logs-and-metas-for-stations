"""
通过yaml文件添加设备分类信息
"""
import yaml
from django.core.management.base import BaseCommand
from django.shortcuts import get_object_or_404

from instruments.models import InstrumentCategory


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "basic_info", type=str, help="The file that contains the basic info"
        )

    def handle(self, *args, **kwargs):
        basic_info = kwargs["basic_info"]
        with open(f"{basic_info}.yaml") as file:
            info = file.read()
            d = yaml.load(info, Loader=yaml.FullLoader)
            for k, v in d.items():
                InstrumentCategory.objects.get_or_create(name=k)
                parent_cat = InstrumentCategory.objects.get(name=k)
                for c in v:
                    InstrumentCategory.objects.get_or_create(name=c, parent=parent_cat)

        self.stdout.write(
            self.style.SUCCESS("Seismic Instruments imported successfully!")
        )
