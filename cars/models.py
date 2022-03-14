from django.db import models

# Create your models here.

# car class is considered a django ora model
# this is considered a code first approach.
class Car(models.Model):
  make = models.CharField(max_length=255)
  model = models.CharField(max_length=255)
  year = models.IntegerField()
  price = models.DecimalField(max_digits=8, decimal_places=2)