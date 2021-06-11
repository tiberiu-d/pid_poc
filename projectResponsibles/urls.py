from django.urls import path
from .views import (
    responsible_list,
    responsible_detail
)

app_name = "projectResponsibles"

urlpatterns = [
    path('', responsible_list),
    path('<pk>/', responsible_detail),
]
