from rest_framework.routers import DefaultRouter
from .views import AuthenticationViewSet

router = DefaultRouter()
router.register(r'auth', AuthenticationViewSet, 'auth')
urlpatterns = router.urls
