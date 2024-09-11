from django.urls import path, include

from. import views

urlpatterns = [
    path('', views.main),
    path('staff/', include('main.staff.urls')),
    path('position/', include('main.position.urls')),
    path('shift/', include('main.shift.urls')),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
]
