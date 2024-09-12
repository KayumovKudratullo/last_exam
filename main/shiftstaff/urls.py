
from django.urls import path, include

from . import views

urlpatterns = [
    path('list/', views.list, name='staffShift_list' ),
    path('create/', views.create, name='staffShift_create' ),
    path('detail/<int:id>/', views.detail, name='staffShift_detail'),
    path('delete/<int:id>/', views.delete, name='staffShift_delete'),
    path('update/<int:id>/', views.update, name='staffShift_update'),
]