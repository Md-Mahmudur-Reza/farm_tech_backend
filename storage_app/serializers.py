from rest_framework import serializers
from .models import Storage


class StorageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = '__all__'