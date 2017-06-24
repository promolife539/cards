from django.db import models


class Card(models.Model):
    en_meaning = models.CharField(max_length=500)
    ru_meaning = models.CharField(max_length=500)
    example = models.CharField(max_length=500)
    extra_info = models.CharField(max_length=500)
    is_active = models.BooleanField(default=True)

# Create your models here.
