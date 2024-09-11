
from django.urls import path, include

from . import views

urlpatterns = [
    path('list/', views.list, name='shift_list' ),
    path('create/', views.create, name='shift_create' ),
    path('delete/<int:id>/', views.delete, name='shift_delete'),
    path('update/<int:id>/', views.update, name='shift_update'),
]