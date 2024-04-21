from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('accounts.urls')),
    path('', SpectacularSwaggerView.as_view(), name='swagger_ui'),
    path('schema/',SpectacularAPIView.as_view(), name='schema'),
]
