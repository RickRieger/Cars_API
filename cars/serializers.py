from rest_framework import serializers
from .models import Car

class CarSerilaizer(serializers.ModelSerializer):
  class Meta: 
    model = Car
    fields = ['id', 'make', 'model', 'year', 'price']