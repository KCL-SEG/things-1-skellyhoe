from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Thing(models.Model):
    name = models.CharField(max_length=30, blank=False, unique=True)
    description = models.CharField(max_length=120, blank=True, unique=False)
    quantity = models.IntegerField(
    blank=False,
    validators=[
        MaxValueValidator(max_value=100),
        MinValueValidator(min_value=0)
    ])
