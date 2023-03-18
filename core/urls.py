from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="CYBERCORP API",
        default_version='v0.1',
        description="Tests de los endpoints",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[AllowAny]
)

urlpatterns = [
    # path('admin/', admin.site.urls),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger',
            cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc',
            cache_timeout=0), name='schema-redoc'),
    # path(
    #     "auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"
    # ),
    # path(
    #     "auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"
    # ),
    # path("auth/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("inventory/", include('app.inventory.api.routers')),
    path('sale/', include('app.sales.api.routers')),
    path('almacen/', include('app.almacen.api.routers')),
    path('users/', include('app.users.api.routers')),
    path('auth/', include('app.authentication.api.routers'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
