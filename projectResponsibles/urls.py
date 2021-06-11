from django.urls import path
from .views import (
    responsible_list,
    responsible_detail,
    responsible_create,
)

app_name = "projectResponsibles"

urlpatterns = [
    path('', responsible_list),
    path('<int:pk>/', responsible_detail),
    path('create/', responsible_create),
]
