from django.urls import path, include

from. import views

urlpatterns = [
    path('', views.main, name='main'),
    path('staff/', include('main.staff.urls')),
    path('position/', include('main.position.urls')),
    path('staffShift/', include('main.shiftstaff.urls')),
    path('shift/', include('main.shift.urls')),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('attendance/', views.attendance, name='attendance_list'),
    path('logout/', views.log_out, name='logout')
]
