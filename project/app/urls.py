from django.urls import path
from . import views

urlpatterns = [
    path('', views.Overview, name='about'),
    path('add/', views.addStudent, name='add-student'),
    path('update/<int:pk>', views.update, name='update-student'),
    path('modify/<int:pk>', views.modify, name='modify-student'),
    path('list/', views.listStudents, name="List-students"),
    path('delete/<int:pk>', views.removeStudent, name="delete-student")
]
