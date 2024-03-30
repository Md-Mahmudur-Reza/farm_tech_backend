from django.db import models
from django.utils.translation import gettext_lazy as _


class ProvinceChoices(models.TextChoices):
    ALBERTA = 'Alberta', _('Alberta')
    BRITISH_COLUMBIA = 'British Columbia', _('British Columbia')
    MANITOBA = 'Manitoba', _('Manitoba')
    NEW_BRUNSWICK = 'New Brunswick', _('New Brunswick')
    NEWFOUNDLAND = 'Newfoundland', _('Newfoundland')
    NOVA_SCOTIA = 'Nova Scotia', _('Nova Scotia')
    NORTHWEST_TERRITORIES = 'Northwest Territories', _('Northwest Territories')
    NUNAVUT = 'Nunavut', _('Nunavut')
    ONTARIO = 'Ontario', _('Ontario')
    PRINCE_EDWARD_ISLAND = 'Prince Edward Island', _('Prince Edward Island')
    QUEBEC = 'Quebec', _('Quebec')
    SASKATCHEWAN = 'Saskatchewan', _('Saskatchewan')
    YUKON = 'Yukon', _('Yukon')

class SoilTypeChoices(models.TextChoices):
    CLAY = 'Clay', _('Clay')
    LOAM = 'Loam', _('Loam')
    SAND = 'Sand', _('Sand')
    CLAY_LOAM = 'Clay loam', _('Clay loam')
    SANDY_LOAM = 'Sandy loam', _('Sandy loam')
    LOAMY_SAND = 'Loamy Sand', _('Loamy Sand')
    SANDY_CLAY = 'Sandy Clay', _('Sandy Clay')
    PEAT = 'Peat', _('Peat')
    CHALK = 'Chalk', _('Chalk')
    SILT = 'Silt', _('Silt')

class ProductionMethodChoices(models.TextChoices):
    CONVENTIONAL = 'Conventional', _('Conventional')
    ORGANIC = 'Organic', _('Organic')


class Crop(models.Model):
    region = models.CharField(
        max_length=100,
        choices=ProvinceChoices.choices,
        null = True,
    )
    soil = models.CharField(
        max_length=100,
        choices=SoilTypeChoices.choices,
        null = True,
    )
    method = models.CharField(
        max_length=100,
        choices=ProductionMethodChoices.choices,
        null = True,
    )