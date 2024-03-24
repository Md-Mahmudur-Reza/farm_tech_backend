from rest_framework import serializers
from .models import ExtendedUser, FarmerDetail, Land, LandApplication, LandAgreement
# from django.contrib.auth.models import User
from django.utils.timezone import now
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, style={'input_type': 'password'})

class ExtendedUserSerializers(serializers.ModelSerializer):
    # extendeduser_name = serializers.SerializerMethodField()
    user_name = serializers.ReadOnlyField(source = 'user.username')
    class Meta:
        model = ExtendedUser
        fields = ['id','user','user_name', 'designation', 'about_me']

    # same thing
    # def get_extendeduser_name(self, obj):
    #     user = User.objects.get(id=obj.user.id)
    #     return user.username


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


class LandApplicationSerializers(serializers.ModelSerializer):
    landowner_name = serializers.ReadOnlyField(source = 'extendeduser.user.username')
    farmer_name = serializers.ReadOnlyField(source = 'extendeduser.user.username')
    land_street_address = serializers.ReadOnlyField(source = 'land.street_address')
    class Meta:
        model = LandApplication
        fields = ['id','landowner', 'landowner_name', 'farmer','farmer_name', 'landid', 'land_street_address', 'application_date','farmer_interested_to_produce']


class LandAgreementSerializers(serializers.ModelSerializer):
    landowner_name = serializers.ReadOnlyField(source = 'extendeduser.user.username')
    farmer_name = serializers.ReadOnlyField(source = 'extendeduser.user.username')
    class Meta:
        model = LandAgreement
        fields = ['id','landowner', 'landowner_name', 'farmer','farmer_name', 'landid', 'agreement_duration', 'agreement_starting_date','product_planning_to_produce', 'facility_and_equipment_agreed_to', 'agreement_description']