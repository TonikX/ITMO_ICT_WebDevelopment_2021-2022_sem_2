from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import *


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=20, blank=True, null=True, unique=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Worker(models.Model):
    name = models.CharField(max_length=100, default=' ')
    passport = models.CharField(max_length=100, blank=True, null=True)
    position = models.CharField(max_length=100)
    salary = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name}'


class Chicken(models.Model):
    breed = models.ForeignKey('Breed', on_delete=models.CASCADE)
    weight = models.IntegerField(default=0)
    age = models.IntegerField(default=0)
    egg_amount = models.IntegerField(default=0)
    cage = models.ForeignKey('Cage', on_delete=models.CASCADE)
    prev_eggs = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return f'{self.breed} {self.cage}'


class Breed(models.Model):
    breed = models.CharField(max_length=50)
    avg_eggs = models.IntegerField(default=0)
    avg_weight = models.IntegerField(default=0)
    diet = models.TextField(verbose_name='Diet for this breed')

    def __str__(self):
        return self.breed


class Cage(models.Model):
    shed = models.IntegerField(default=0)
    row = models.IntegerField(default=0)
    cage = models.IntegerField(default=0)
    square = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.shed} {self.row} {self.cage}'


class Working(models.Model):
    name = models.ForeignKey('Worker', on_delete=models.CASCADE)
    cage = models.ForeignKey('Cage', on_delete=models.CASCADE, blank=True, null=True)
    work_types = (
        ('cl', 'cleaning'),
        ('fd', 'giving food'),
        ('med', 'giving medicine')
    )
    work_type = models.CharField(max_length=3, choices=work_types)
    work_date = models.DateField()
    work_status = models.BooleanField(default=False)
    details = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.work_date} {self.cage} {self.name}'


def get_path(instance, filename):
    return f'worker_photo_{instance.worker.id}/{filename}'


class WorkerPhoto(models.Model):
    worker = models.ForeignKey('Worker', on_delete=models.CASCADE, verbose_name='Photo')
    filename = models.CharField(max_length=100, blank=True, null=True)
    filesize = models.IntegerField(blank=True, null=True)
    file = models.FileField(validators=[file_validation], upload_to=get_path)

    def save(self, *args, **kwargs):
        self.filename = self.file.name
        self.filesize = self.file.size
        super(WorkerPhoto, self).save(*args, **kwargs)
