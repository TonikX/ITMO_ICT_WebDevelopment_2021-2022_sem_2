from django.db.models.signals import post_save, pre_save, pre_delete
from django.dispatch import receiver
from django.db.models import ObjectDoesNotExist
from .models import *


@receiver(post_save, sender=Chicken)
def create_breed(sender, instance, created, **kwargs):
    if created:
        print(f'\nA new chicken in {instance.cage} cage appeared!')


@receiver(pre_save, sender=Chicken)
def update_chicken(sender, instance, **kwargs):
    try:
        old = Chicken.objects.get(id=instance.id)
        instance.prev_eggs = old.egg_amount
        if instance.prev_eggs > instance.egg_amount:
            print(f'The {instance.id} chicken gives less eggs! Call the vet. \n'
                  f'Previous month: {instance.prev_eggs}\n'
                  f'This month: {instance.egg_amount}\n')
        else:
            print(f'Everything is all right with the {instance.id} chicken!')
    except ObjectDoesNotExist:
        pass


@receiver(pre_delete, sender=Chicken)
def delete_chicken(sender, instance, **kwargs):
    with open('dead_chickens.txt', 'a') as f:
        f.write(f'\nThe chicken {instance.id} died. Call the crematorium(((')
