from django.contrib import admin
from . import models


# Admin Customization for Position Model
@admin.register(models.Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("name",)  # Corrected the tuple
    list_filter = ("name",)   # Comma added to make it a tuple
    search_fields = ("name",) # You can add search functionality


# Admin Customization for Employee Model
@admin.register(models.Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("full_name", "is_active", "position")  # Display these fields
    list_filter = ("is_active", "position")                # Filters for easier navigation
    search_fields = ("full_name",)                         # Search by full name


# Admin Customization for Shift Model
@admin.register(models.Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ("shift_type", "start_time", "end_time")
    search_fields = ("shift_type",)


# Admin Customization for StaffShift Model
@admin.register(models.StaffShift)
class StaffShiftAdmin(admin.ModelAdmin):
    list_display = ("employee", "shift")
    list_filter = ("shift",)


# Admin Customization for StaffAttendance Model
@admin.register(models.StaffAttendance)
class StaffAttendanceAdmin(admin.ModelAdmin):
    list_display = ("staff_shift", "check_in", "check_out",)
    list_filter = ("check_in", "staff_shift",)
    search_fields = ("staff_shift_employee__full_name",)  # Enables searching by staff name
