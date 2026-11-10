from django.db import models
from materials.choices import MaterialChoices

class Material(models.Model):
    name = models.CharField(
        max_length=100,
        choices=MaterialChoices.choices,
        default=MaterialChoices.PLA_SERIES
    )