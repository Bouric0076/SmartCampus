# filepath: admins/forms.py
from django import forms

from students.models import Timetable
from .models import Course, Unit, Notice, Event, AdminProfile

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = '__all__'

class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        exclude = ['date_posted', 'posted_by']

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ['date_posted']

class AdminProfileForm(forms.ModelForm):
    class Meta:
        model = AdminProfile
        fields = ['phone_number', 'profile_pic']


class AdminProfileForm(forms.ModelForm):
    class Meta:
        model = AdminProfile
        fields = ['user', 'phone_number']


class TimetableForm(forms.ModelForm):
    class Meta:
        model = Timetable
        fields = ['unit', 'day_of_the_week', 'start_time', 'end_time', 'venue']

