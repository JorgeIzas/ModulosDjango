from rest_framework import serializers
from .models import ventas

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ventas
        fields = '__all__'
