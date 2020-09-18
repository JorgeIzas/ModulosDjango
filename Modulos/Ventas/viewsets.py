from rest_framework import viewsets
from .models import ventas
from .serializer import VentaSerializer

class VentaViewSet(viewsets.ModelViewSet):
    queryset = ventas.objects.all()
    serializer_class = VentaSerializer
