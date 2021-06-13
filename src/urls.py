"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

# from projectTypes.views import type_list
# from projectResponsibles.views import responsible_list
from Links.views import links_view

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('projects/types/view/', type_list),
    path('links/view/', links_view),
    # pointing to new apps
    path('projects/responsibles/',include('projectResponsibles.urls', namespace='projectResponsibles')),
    path('projects/types/',include('projectTypes.urls', namespace='projectTypes')),
]
