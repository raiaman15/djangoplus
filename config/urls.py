"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from upload.views import image_upload

urlpatterns = [
    # Django admin
    path('infroid-backend/', admin.site.urls),

    # User management
    path('accounts/', include('allauth.urls')),

    # Local apps
    path("upload/", image_upload, name="upload"),
]

if bool(settings.DEBUG) == True:
    """Development Specific Routes"""
    from django.contrib import admin
    from config.settings import local
    from django.conf.urls.static import static
    urlpatterns += static(local.STATIC_URL,
                          document_root=local.STATIC_ROOT)
    urlpatterns += static(local.MEDIA_URL,
                          document_root=local.MEDIA_ROOT)
else:
    """Production Specific Routes"""
    urlpatterns += path('admin/', include('admin_honeypot.urls',
                                          namespace='admin_honeypot')),
