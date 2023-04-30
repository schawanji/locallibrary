"""locallibrary URL Configuration
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
#Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/',include('catalog.urls')),
    path('', RedirectView.as_view(url='catalog/', permanent=True)), path('', RedirectView.as_view(url='catalog/', permanent=True)),
    # Add Django site authentication urls (for login, logout, password management)
    path('accounts/', include('django.contrib.auth.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
