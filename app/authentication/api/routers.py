from rest_framework.routers import DefaultRouter
from .views import AuthenticationViewSet

router = DefaultRouter()
router.register(r'', viewset=AuthenticationViewSet, basename='auth')
urlpatterns = router.urls
