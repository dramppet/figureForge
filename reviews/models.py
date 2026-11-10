from django.core.validators import MinValueValidator, MaxValueValidator

from django.db import models

class Review(models.Model):
    author_name = models.CharField(
        max_length=100,
    )
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )
    comment = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    figure = models.ForeignKey(
        to='figures.Figure',
        on_delete=models.CASCADE,
        related_name='reviews_author'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.author_name} - {self.figure}'
