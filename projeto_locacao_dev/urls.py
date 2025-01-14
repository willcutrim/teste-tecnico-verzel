from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

schema_view = get_schema_view(
    openapi.Info(
        title="API de Alocação de Desenvolvedores",
        default_version='v1',
        description="API para gerenciar e realizar a alocação de desenvolvedores de software em projetos.",
    ),
    public=True,
    permission_classes=(IsAuthenticated,),
)

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('api/alocacoes/', include('alocacoes.urls')),
    path('api/projetos/', include('projetos.urls')),
    path('api/tecnologias/', include('tecnologias.urls')),
    path('api/programadores/', include('programadores.urls')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
