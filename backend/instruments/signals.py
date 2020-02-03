from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import SeismicInstrumentEntity, InstrumentModel


@receiver(post_save, sender=SeismicInstrumentEntity)
def create_entity_cal_model_total(sender, instance, created, *args, **kwargs):
    if created:
        instrument_model = instance.instrument_model
        instrument_model.total = SeismicInstrumentEntity.objects.filter(
            instrument_model=instrument_model).count()
        instrument_model.save()


@receiver(post_delete, sender=SeismicInstrumentEntity)
def delete_entity_cal_model_total(sender, instance, **kwargs):
    instrument_model = instance.instrument_model
    instrument_model.total = SeismicInstrumentEntity.objects.filter(
        instrument_model=instrument_model).count()
    instrument_model.save()