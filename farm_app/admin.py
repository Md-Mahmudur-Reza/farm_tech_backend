from django.contrib import admin
from .models import ExtendedUser, FarmerDetail, Land

admin.site.register(ExtendedUser)
admin.site.register(FarmerDetail)
admin.site.register(Land)