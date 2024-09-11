
from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list, name='position_list' ),
    path('create/', views.create, name='position_create' ),
    path('update/<int:id>/', views.update, name='position_update' ),
    path('delete/<int:id>/', views.delete, name='position_delete' )
]