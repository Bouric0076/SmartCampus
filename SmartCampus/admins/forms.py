# filepath: admins/forms.py
from django import forms
from .models import AdminProfile

class AdminProfileForm(forms.ModelForm):
    class Meta:
        model = AdminProfile
        fields = ['user', 'phone_number', 'address']