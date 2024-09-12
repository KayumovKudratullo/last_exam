from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Employee(models.Model):
    full_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)  # Fixed typo here
 
    def __str__(self):
        return self.full_name
    

class Shift(models.Model):
    shift_type = models.CharField(max_length=50)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.shift_type


class StaffShift(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.employee} -> {self.shift}"


class StaffAttendance(models.Model):
    staff_shift = models.ForeignKey(StaffShift, on_delete=models.SET_NULL, null=True)
    check_in = models.TimeField()
    check_out = models.TimeField()

    def __str__(self):
        return f"{self.staff_shift.employee.full_name} - {self.check_in}"       