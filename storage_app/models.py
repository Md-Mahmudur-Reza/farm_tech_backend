from django.db import models
from django.utils.translation import gettext_lazy as _


class ProductChoices(models.TextChoices):
    FIELD_CROPS = 'Field crops (grains or beans)', _('Field crops (grains or beans)')
    FLOWERS = 'Flowers', _('Flowers')
    FRUITS_BERRIES_GRAPES = 'Fruit/berries/grapes', _('Fruit/berries/grapes')
    HAY_FORAGE_CROPS = 'Hay or forage crops', _('Hay or forage crops')
    HERBS = 'Herbs', _('Herbs')
    LIVESTOCK = 'Livestock', _('Livestock')
    SEEDS = 'Seeds, seedlings or nursery stock', _('Seeds, seedlings or nursery stock')
    VEGETABLES = 'Vegetables', _('Vegetables')
    OTHER_PRODUCTS = 'Other products', _('Other products')

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


class Storage(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    province = models.CharField(
        max_length=100,
        choices=ProvinceChoices.choices,
        null = True
    )
    capacity = models.PositiveIntegerField()
    crop_type = models.CharField(
        max_length=100,
        choices=ProductChoices.choices,
        null = True,
    )
    min_renting_period = models.PositiveIntegerField()

    def __str__(self):
        return self.name