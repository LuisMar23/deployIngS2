from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet, ProveedorViewSet, SedeViewSet

router = DefaultRouter()
router.register(r'producto', ProductoViewSet, 'producto')
router.register(r'supplier', ProveedorViewSet, 'supplier')
router.register(r'sede', SedeViewSet, 'sede')
urlpatterns = router.urls
