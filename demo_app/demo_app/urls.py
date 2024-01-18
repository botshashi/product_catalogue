
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('auth_service.urls')),
    path('api/', include('product_catalogue_service.urls')),
]

