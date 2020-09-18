from rest_framework import routers
from .viewsets import VentaViewSet

router = routers.SimpleRouter()
router.register('Ventas', VentaViewSet)

urlpatterns = router.urls
