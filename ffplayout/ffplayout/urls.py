"""ffplayout URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
import os
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include(
         'rest_framework.urls', namespace='rest_framework')),
    path('auth/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh')
]


# dynamic url loader
for dir in os.listdir(settings.APPS_DIR):
    if os.path.isdir(os.path.join(settings.APPS_DIR, dir)):
        app_name = 'apps.{}'.format(dir)

        _path = path('api/', include(
            '{}.urls'.format(app_name),
            namespace='{}'.format(app_name.split('.')[1])))

        if _path not in urlpatterns:
            urlpatterns += (_path, )
