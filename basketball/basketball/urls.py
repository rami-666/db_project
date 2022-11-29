"""basketball URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from quickstart import urls as todo_urls


# from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin-interface/logo/flc_design2022112885556.png', RedirectView.as_view(url=staticfiles_storage.url('flc_design2022112885556.png'))),
    path('admin-interface/favicon/favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('favicon.ico'))),
    path('api-auth', include('rest_framework.urls')),
    path('quickstart/', include(todo_urls)),
]
