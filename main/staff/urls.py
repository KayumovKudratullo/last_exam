
from django.urls import path, include

from . import views

urlpatterns = [
    path('list/', views.list, name='staff_list' ),
    path('create/', views.create, name='staff_create' ),
    path('detail/<int:id>/', views.detail, name='staff_detail'),
    path('delete/<int:id>/', views.delete, name='staff_delete'),
    path('update/<int:id>/', views.update, name='staff_update'),
]