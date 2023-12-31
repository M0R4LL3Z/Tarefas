from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('newtask/', views.newtask, name='newtask'),
    path('edit/<int:id>', views.editTask, name="edit-task"),
    path('delete/<int:id>', views.deleteTask, name="delete-task"),
    path('changestatus/<int:id>', views.changeStatus, name="change-status"),
    path('Email/',views.envia_email, name='envia_email'),
    path('task/<int:id>', views.taskView, name="task-view"),
]