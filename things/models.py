from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Thing(models.Model):
    name = models.CharField(max_length=30, blank=False, unique=True)
    description = models.CharField(max_length=120, blank=True, unique=False)
    quantity = models.IntegerField(
    unique=False,
    validators=[
        MinValueValidator(limit_value=0),
        MaxValueValidator(limit_value=100),

    ])
