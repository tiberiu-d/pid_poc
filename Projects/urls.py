from django.urls import path

from .views import (
    project_list,
    project_create,
    project_read,
    project_update,
    project_delete
)

app_name = "Projects"

urlpatterns = [
    path('', project_list, name='project-list'),
    path('create/', project_create, name='project-create'),
    path('<int:pk>/view/', project_read, name='project-read'),
    path('<int:pk>/update/', project_update, name='project-update'),
    path('<int:pk>/delete/', project_delete, name='project-delete'),
]
