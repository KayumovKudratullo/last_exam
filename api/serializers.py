from rest_framework import serializers
from main import models

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Position
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = ['id', 'full_name']


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = '__all__'

class ShiftSerializer(serializers.ModelSerializer):
    # Customize the start_time and end_time fields to handle different formats
    start_time = serializers.TimeField(input_formats=['%H:%M', ])
    end_time = serializers.TimeField(input_formats=['%H:%M', ])

    class Meta:
        model = models.Shift
        fields = ['shift_type', 'start_time', 'end_time']


class StaffShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StaffShift
        fields = '__all__'


class StaffAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StaffAttendance
        fields = '__all__'
