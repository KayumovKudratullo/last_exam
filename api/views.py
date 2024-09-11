from rest_framework import generics, permissions

from main import models
from .serializers import (
    PositionSerializer,
    EmployeeSerializer,
    ShiftSerializer,
    StaffShiftSerializer,
    StaffAttendanceSerializer
)


# Position Views
class PositionListCreateView(generics.ListCreateAPIView):
    queryset = models.Position.objects.all()
    serializer_class = PositionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PositionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Position.objects.all()
    serializer_class = PositionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# Employee Views
class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class EmployeeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# Shift Views
class ShiftListCreateView(generics.ListCreateAPIView):
    queryset = models.Shift.objects.all()
    serializer_class = ShiftSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ShiftRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Shift.objects.all()
    serializer_class = ShiftSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# StaffShift Views
class StaffShiftListCreateView(generics.ListCreateAPIView):
    queryset = models.StaffShift.objects.all()
    serializer_class = StaffShiftSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class StaffShiftRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.StaffShift.objects.all()
    serializer_class = StaffShiftSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# StaffAttendance Views
class StaffAttendanceListCreateView(generics.ListCreateAPIView):
    queryset = models.StaffAttendance.objects.all()
    serializer_class = StaffAttendanceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class StaffAttendanceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.StaffAttendance.objects.all()
    serializer_class = StaffAttendanceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
