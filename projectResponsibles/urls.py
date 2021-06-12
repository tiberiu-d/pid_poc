from django.urls import path
from .views import (
    responsible_list, #L
    responsible_detail, #R
    responsible_create, #C
    responsible_update, #U
    responsible_delete, #D
)

app_name = "projectResponsibles"

urlpatterns = [
    path('', responsible_list, name='responsible-list'),
    path('<int:pk>/', responsible_detail, name='responsible-detail'),
    path('<int:pk>/update/', responsible_update, name='responsible-update'),
    path('<int:pk>/delete/', responsible_delete, name='responsible-delete'),
    path('create/', responsible_create, name='responsible-create'),
]
