from django.contrib import admin
from .models import ExtendedUser, FarmerDetail, Land, LandApplication, LandAgreement

admin.site.register(ExtendedUser)
admin.site.register(FarmerDetail)
admin.site.register(Land)
admin.site.register(LandApplication)
admin.site.register(LandAgreement)