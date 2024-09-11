from django.urls import path
from . import views

urlpatterns = [
    # Position URLs
    path('positions/', views.PositionListCreateView.as_view(), name='position-list-create'),
    path('positions/<int:pk>/', views.PositionRetrieveUpdateDestroyView.as_view(), name='position-detail'),

    # Employee URLs
    path('employees/', views.EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', views.EmployeeRetrieveUpdateDestroyView.as_view(), name='employee-detail'),

    # Shift URLs
    path('shifts/', views.ShiftListCreateView.as_view(), name='shift-list-create'),
    path('shifts/<int:pk>/', views.ShiftRetrieveUpdateDestroyView.as_view(), name='shift-detail'),

    # StaffShift URLs
    path('staff-shifts/', views.StaffShiftListCreateView.as_view(), name='staff-shift-list-create'),
    path('staff-shifts/<int:pk>/', views.StaffShiftRetrieveUpdateDestroyView.as_view(), name='staff-shift-detail'),

    # StaffAttendance URLs
    path('staff-attendance/', views.StaffAttendanceListCreateView.as_view(), name='staff-attendance-list-create'),
    path('staff-attendance/<int:pk>/', views.StaffAttendanceRetrieveUpdateDestroyView.as_view(), name='staff-attendance-detail'),
]
