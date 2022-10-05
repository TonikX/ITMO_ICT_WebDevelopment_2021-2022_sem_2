from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from .models import *

class AdminSerializer(ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = "__all__"


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = "__all__"


class CleaningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cleaning
        fields = "__all__"


class RoomPictureSerializer(ModelSerializer):
    file = serializers.FileField()

    class Meta:
        model = RoomPicture
        fields = ['file', 'room', 'file_size']


class FileUploadsSerializer(ModelSerializer):
    class Meta:
        model = FileUploads
        fields = ['file']
