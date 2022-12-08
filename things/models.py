from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class Thing(models.Model):
    name = models.CharField(max_length=30, unique=True, blank=False)
    description = models.CharField(max_length=120, blank=True)
    quantity = models.IntegerField(default=0, blank=False, null=False, validators=[MinValueValidator(0), MaxValueValidator(100)])
    def __str__(self):
        return self.name