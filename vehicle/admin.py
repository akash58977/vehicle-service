from django.contrib import admin
from .models import Customer, Mechanic, Request, Attendance, Feedback


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "mobile", "address")
    search_fields = ("user__username", "user__first_name", "mobile")


@admin.register(Mechanic)
class MechanicAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "mobile", "skill", "salary", "status")
    list_filter = ("status",)
    search_fields = ("user__username", "user__first_name", "skill")


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "vehicle_name",
        "vehicle_no",
        "customer",
        "mechanic",
        "status",
        "date",
    )
    list_filter = ("status", "category")
    search_fields = ("vehicle_name", "vehicle_brand", "vehicle_model")


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ("id", "mechanic", "date", "present_status")
    list_filter = ("present_status",)


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("id", "by", "date")
    search_fields = ("by", "message")