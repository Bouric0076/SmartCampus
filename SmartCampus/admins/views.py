# filepath: admins/views.py
from django.shortcuts import render, get_object_or_404
from .models import AdminProfile
from .forms import AdminProfileForm

def admin_list(request):
    admins = AdminProfile.objects.all()
    return render(request, 'admins/admin_list.html', {'admins': admins})

def admin_detail(request, pk):
    admin = get_object_or_404(AdminProfile, pk=pk)
    return render(request, 'admins/admin_detail.html', {'admin': admin})