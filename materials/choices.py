from django.db import models

class MaterialChoices(models.TextChoices):
    PLA_SERIES = 'PLA Series', 'PLA'
    PETG_SERIES = 'PETG Series', 'PETG'
    ABS_SERIES = 'ABS Series', 'ABS'
    PA_SERIES = 'PA Series', 'PA'
    TPU_SERIES = 'TPU Series', 'TPU'
    MASTERBATCH_SERIES = ('Masterbatch Series','MB')
