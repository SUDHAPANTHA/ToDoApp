
from django.urls import path
from todo_app import views

urlpatterns = [
    path("", views.todo_list),
    path("delete/<int:pk>/", views.todo_delete),
    path("create/", views.todo_create),
    path("update/<int:id>/", views.todo_update),

]