from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator

class Figure(models.Model):
    title = models.CharField(
        max_length=100,
    )
    character_name=models.CharField(
        max_length=50,
    )
    base_price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0.01)],
    )
    height = models.PositiveIntegerField(
        validators=[MinValueValidator(5)],
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        blank=True,
    )
    manufacturers = models.ForeignKey(
        'manufacturers.Manufacturer',
        on_delete=models.PROTECT,
        related_name='figures',
    )
    materials = models.ManyToManyField(
        'materials.Material',
        related_name='figures_materials',
        blank=False,
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

