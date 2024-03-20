from rest_framework import serializers
from .models import ExtendedUser, FarmerDetail, Land
from django.contrib.auth.models import User
from django.utils.timezone import now

class ExtendedUserSerializers(serializers.ModelSerializer):
    extendeduser_name = serializers.SerializerMethodField()

    class Meta:
        model = ExtendedUser
        fields = '__all__'

    def get_extendeduser_name(self, obj):
        user = User.objects.get(id=obj.user.id)
        return user.username


class FarmerDetailSerializers(serializers.ModelSerializer):
    farmer_name = serializers.SerializerMethodField()

    class Meta:
        model = FarmerDetail
        fields = '__all__'

    def get_farmer_name(self, obj):
        user = User.objects.get(id=obj.extendeduser.user.id)
        return user.username


class LandSerializers(serializers.ModelSerializer):
    land_owner_name = serializers.SerializerMethodField()

    class Meta:
        model = Land
        fields = '__all__'

    def get_land_owner_name(self, obj):
        user = User.objects.get(id=obj.extendeduser.user.id)
        return user.username
