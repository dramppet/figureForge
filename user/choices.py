from django.db import models

class OrderStatusChoices(models.TextChoices):
  PENDING = 'Pending', 'Pen'
  PROCESSING = 'Processing', 'Pro'
  SHIPPED = 'Shipped', 'Ship'
  DELIVERED = 'Delivered', 'Del'
  CANCELLED = 'Cancelled', 'Can'