"""task_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.urls import include

from rest_framework.authtoken.views import obtain_auth_token


admin_str = 'Admin TASK app'
admin.site.site_header = admin_str
admin.site.site_title = admin_str


urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('secret-4dm1n/', admin.site.urls),
    url(r'^api/', include('api.urls', namespace='api'))
]
