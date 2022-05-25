from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import *

@receiver(pre_delete, sender=Rahbariyat)
def delete_rahbariyat(sender, instance, *args, **kwargs):
    if instance.image:
        instance.image.delete()

@receiver(pre_delete, sender=Region)
def delete_region(sender, instance, *args, **kwargs):
    if instance.image_region:
        instance.image_region.delete()
    if instance.image:
        instance.image.delete()

@receiver(pre_delete, sender=Foto_lavhalar)
def delete_foto_lavhalar(sender, instance, *args, **kwargs):
    if instance.foto_lavha:
        instance.foto_lavha.delete()


@receiver(pre_delete, sender=News)
def delete_news(sender, instance, *args, **kwargs):
    if instance.image:
        instance.image.delete()

@receiver(pre_delete, sender=Events)
def delete_events(sender, instance, *args, **kwargs):
    if instance.image:
        instance.image.delete()
