from email.policy import default
from tabnanny import verbose
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

import magic
from django.utils.deconstruct import deconstructible
from django.template.defaultfilters import filesizeformat

class Admin(AbstractUser):
    phone = models.CharField(max_length=14)
    full_name = models.CharField(max_length=255) 

class Room(models.Model):
    ROOM_TYPE = (
        ('4', 'luxe'),
        ('3', '2 beds'),
        ('2', '1 kingsize bed'),
        ('1', '1 bed'))

    number = models.CharField(verbose_name = 'Room Number', max_length=4, primary_key=True, unique=True)
    type = models.CharField(verbose_name = 'Room Type', max_length=1, choices=ROOM_TYPE)
    price = models.IntegerField(verbose_name = 'Price')
    floor = models.IntegerField(verbose_name = 'Floor Number')
    cleaners = models.ManyToManyField('Staff', through='Cleaning')


class RoomPicture(models.Model):
    file = models.ImageField()
    file_name = models.CharField(max_length=255)
    file_size = models.FloatField()
    room = models.ForeignKey(to=Room, on_delete=models.CASCADE)


class Guest(models.Model):
    passport_number = models.CharField(verbose_name = 'Passport Number', max_length=10, unique=True)
    name = models.CharField(verbose_name = 'Guest Name', max_length=100)
    surname = models.CharField(verbose_name = 'Guest Surname', max_length=100)
    middlename = models.CharField(verbose_name = 'Guest Middlename', max_length=100)
    from_location = models.CharField(verbose_name = 'Guest Location', max_length=100)
    check_in_date = models.DateField(verbose_name = 'Guest Check-in Date', default=timezone.now)
    check_out_date = models.DateField(verbose_name = 'Guest Check-out Date', default=timezone.now)
    prev_check_out_date = models.DateField(verbose_name = 'Previous Guest Check-out Date', default=timezone.now)
    room = models.ForeignKey('Room', on_delete=models.PROTECT, related_name='guests')


class Staff(models.Model):
    name = models.CharField(verbose_name = 'Staff Full Name', max_length=100)
    phone = models.CharField(verbose_name="Staff Phone Number", max_length=14, default = '00000000000000')

    def __str__(self):
        return self.name

class Cleaning(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='cleaning')
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='cleaning')
    date_time = models.DateTimeField(verbose_name = 'Cleaning Date')


@deconstructible
class FileValidator(object):
    error_messages = {
        'max_size': ("Ensure this file size is not greater than %(max_size)s."
                     " Your file size is %(size)s."),
        'min_size': ("Ensure this file size is not less than %(min_size)s. "
                     "Your file size is %(size)s."),
        'content_type': "Files of type %(content_type)s are not supported.",
    }

    def __init__(self, max_size=None, min_size=None, content_types=()):
        self.max_size = max_size
        self.min_size = min_size
        self.content_types = content_types

    def __call__(self, data):
        if self.max_size is not None and data.size > self.max_size:
            params = {
                'max_size': filesizeformat(self.max_size),
                'size': filesizeformat(data.size),
            }
            raise ValidationError(self.error_messages['max_size'],
                                  'max_size', params)

        if self.min_size is not None and data.size < self.min_size:
            params = {
                'min_size': filesizeformat(self.min_size),
                'size': filesizeformat(data.size)
            }
            raise ValidationError(self.error_messages['min_size'],
                                  'min_size', params)

        if self.content_types:
            content_type = magic.from_buffer(data.read(), mime=True)
            data.seek(0)

            if content_type not in self.content_types:
                params = {'content_type': content_type}
                raise ValidationError(self.error_messages['content_type'],
                                      'content_type', params)

    def __eq__(self, other):
        return (
                isinstance(other, FileValidator) and
                self.max_size == other.max_size and
                self.min_size == other.min_size and
                self.content_types == other.content_types
        )


file_validator = FileValidator(max_size=1024 * 100,
                               content_types=("image/jpeg",))


class FileUploads(models.Model):
    file = models.FileField(validators=[file_validator])