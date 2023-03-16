from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'egreso', EgresoViewSet)
urlpatterns = router.urls