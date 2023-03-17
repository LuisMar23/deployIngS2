from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, SupplierViewSet, BranchOfficeViewSet

router = DefaultRouter()
router.register(r'producto', ProductViewSet, 'producto')
router.register(r'supplier', SupplierViewSet, 'supplier')
router.register(r'sede', BranchOfficeViewSet, 'sede')
urlpatterns = router.urls
