from django.core.management.base import BaseCommand
from django.shortcuts import get_object_or_404

from instruments.models import Department, InstrumentCategory, InstrumentModel, SeismicInstrumentEntity


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'instrument_entities_file', type=str, help='The file that contains the seismic instrument entities info')

    def handle(self, *args, **kwargs):
        instrument_entities_file = kwargs['instrument_entities_file']
        with open(f'{instrument_entities_file}.txt') as file:
            for line in file:
                line = line.strip('\n')
                sn, model, param, category, belong, status = line.split(',')
                category_parent = get_object_or_404(InstrumentCategory, name='测震设备')
                InstrumentCategory.objects.get_or_create(name=category, parent=category_parent)
                cat = InstrumentCategory.objects.get(name=category)

                InstrumentModel.objects.get_or_create(name=model, param=param, category=cat, has_sn=True)
                instrument_model = InstrumentModel.objects.get(name=model, param=param)

                Department.objects.get_or_create(name=belong)
                department = Department.objects.get(name=belong)

                defaults = {'instrument_model': instrument_model, 'belong': department, 'status': status}

                entity, created = SeismicInstrumentEntity.objects.update_or_create(sn=sn, defaults=defaults)

        self.stdout.write(self.style.SUCCESS('Seismic Instruments imported successfully!'))
