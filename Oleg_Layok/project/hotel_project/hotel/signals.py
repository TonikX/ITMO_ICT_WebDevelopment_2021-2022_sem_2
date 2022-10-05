import copy

from django.db.models.signals import post_save, pre_save, post_init, post_delete
from django.dispatch import receiver

from hotel.models import Guest


@receiver(post_save, sender=Guest)
def save_logic(sender, instance, created, **kwargs):
    if created:
        print("New Guest created")


@receiver(pre_save, sender=Guest)
def update(sender, instance, **kwargs):
    try:
        prev_instance = Guest.objects.get(id=instance.id)
        instance.prev_check_out_date = prev_instance.check_out_date
        print("Prev check-out date updated")
    except:
        pass



@receiver(post_delete, sender=Guest)
def delete_log(sender, instance, **kwargs):
    print(f"Delete {instance.name}")