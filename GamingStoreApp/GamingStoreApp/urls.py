"""
URL configuration for GamingStoreApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from task1.views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', sign_up_by_html),
    path('django_sign_up/', sign_up_by_django),
    path('platform/', platform_page_index),
    path('platform/games/', catalog_page_index),
    path('platform/cart/', cart_page_index),
    path('platform/news/', news_index),
    path('menu/', menu_page_index)
    # path('index/', TemplateView.as_view(template_name='index2.html'))
]
