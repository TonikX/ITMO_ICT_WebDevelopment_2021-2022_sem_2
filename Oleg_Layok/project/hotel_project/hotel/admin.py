from django.contrib import admin
from django.contrib.admin import ModelAdmin

from hotel.models import *

@admin.register(Admin)
class AdminAdmin(ModelAdmin):
    pass

@admin.register(Room)
class RoomAdmin(ModelAdmin):
    pass

@admin.register(Guest)
class GuestAdmin(ModelAdmin):
    pass

@admin.register(Cleaning)
class CleaningAdmin(ModelAdmin):
    pass

@admin.register(Staff)
class StaffAdmin(ModelAdmin):
    pass


admin.site.register(RoomPicture)
admin.site.register(FileUploads)