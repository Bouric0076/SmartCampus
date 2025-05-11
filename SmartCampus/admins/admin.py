# filepath: admins/admin.py
from django.contrib import admin

from students.models import Enrollment, FeePayment, Grade, StudentProfile, Timetable
from .models import AdminProfile, Event, Course, Unit, Notice
from django.contrib.auth.models import User

@admin.register(AdminProfile)
class AdminProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'date_joined')
    search_fields = ('user__username', 'phone_number')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'head_of_department', 'phone_number')
    search_fields = ('name', 'head_of_department')
    list_filter = ('head_of_department',)

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('course', 'name', 'unit_code', 'lecture_hours')
    search_fields = ('course__name', 'name', 'unit_code')
    list_filter = ('course',)

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted', 'posted_by')
    search_fields = ('title', 'posted_by')
    list_filter = ('date_posted',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'time', 'venue')
    search_fields = ('title', 'venue')
    list_filter = ('date',)

@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):
    list_display = ('unit', 'day_of_the_week', 'start_time', 'end_time', 'venue')
    search_fields = ('unit__name', 'day_of_the_week', 'venue')
    list_filter = ('unit', 'day_of_the_week')

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'unit')
    search_fields = ('student__user__username', 'unit__name')
    list_filter = ('unit',)

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('enrollment', 'grade', 'marks')
    search_fields = ('enrollment__student__user__username', 'grade')
    list_filter = ('enrollment__unit',)

@admin.register(FeePayment)
class FeePaymentAdmin(admin.ModelAdmin):
    list_display = ('student', 'amount_paid', 'payment_date', 'payment_method', 'reference_number')
    search_fields = ('student__user__username', 'payment_method', 'reference_number')
    list_filter = ('payment_date', 'payment_method')

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'reg_no', 'course', 'date_of_birth', 'phone_number')
    search_fields = ('user__username', 'reg_no', 'course__name')
    list_filter = ('course',)
    list_editable = ('course', 'date_of_birth', 'phone_number')


