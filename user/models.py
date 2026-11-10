from django.db import models
from user.choices import OrderStatusChoices
from figures.models import Figure
from materials.models import Material


class Client(models.Model):
    name = models.CharField(
        max_length=100,
    )
    email = models.EmailField(
        max_length=100,
        unique=True,
    )
    status_order = models.CharField(
        max_length=100,
        choices=OrderStatusChoices.choices,
        default=OrderStatusChoices.PENDING,
    )

    figure = models.ForeignKey(
        to=Figure,
        related_name='figures_type',
        on_delete=models.CASCADE
    )

    chose_material = models.ForeignKey(
        to=Material,
        related_name='materials_type',
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f'{self.name}: {self.figure}'

