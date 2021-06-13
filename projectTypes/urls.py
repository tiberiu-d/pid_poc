from django.urls import path
from .views import (
    types_list,
    types_create,
    types_read,
    types_update,
    types_delete,
)

app_name = "projectTypes"

urlpatterns = [
    path('', types_list, name="projTypes-list"),
    path('create/', types_create, name="projTypes-create"),
    path('<int:pk>/details/', types_read, name="projTypes-read"),
    path('<int:pk>/update/', types_update, name="projTypes-update"),
    path('<int:pk>/delete/', types_delete, name="projTypes-delete"),
]
