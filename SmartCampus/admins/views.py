# filepath: admins/views.py
from django.shortcuts import render, get_object_or_404

from students.models import Timetable
from .models import AdminProfile
from .forms import AdminProfileForm, TimetableForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Course, Unit, Notice, Event, AdminProfile
from django.contrib.auth.models import User
from .forms import CourseForm, UnitForm, NoticeForm, EventForm, AdminProfileForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Count
import json
from django.core.exceptions import ObjectDoesNotExist

# Utility to check if user is admin (customize as needed)
def is_admin(user):
    return user.is_staff or hasattr(user, 'adminprofile')


# --- DASHBOARD VIEW ---

def admin_dashboard(request):
    if not request.user.is_staff:
        return redirect('home')

    # Ensure AdminProfile exists
    try:
        profile = AdminProfile.objects.get(user=request.user)
    except AdminProfile.DoesNotExist:
        profile = AdminProfile.objects.create(user=request.user)

    # Units per course
    course_unit_data = Course.objects.annotate(unit_count=Count('unit'))
    course_names = [course.name for course in course_unit_data]
    unit_counts = [course.unit_count for course in course_unit_data]

    # Timetable distribution by day
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    timetable_distribution = [
        Timetable.objects.filter(day_of_the_week=day).count() for day in days
    ]

    context = {
        'course_count': Course.objects.count(),
        'unit_count': Unit.objects.count(),
        'event_count': Event.objects.count(),
        'notice_count': Notice.objects.count(),
        'timetable_count': Timetable.objects.count(),
        'profile': profile,  # pass the created/fetched profile

        # chart data
        'course_names': json.dumps(course_names),
        'unit_counts': json.dumps(unit_counts),
        'timetable_days': json.dumps(days),
        'timetable_counts': json.dumps(timetable_distribution),
    }
    return render(request, 'admins/dashboard.html', context)

# --- COURSE VIEWS ---

@login_required
@user_passes_test(is_admin)
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'admins/course_list.html', {'courses': courses})

@login_required
@user_passes_test(is_admin)
def course_create(request):
    form = CourseForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Course created successfully.")
        return redirect('course_list')
    return render(request, 'admins/course_form.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def course_update(request, pk):
    course = get_object_or_404(Course, pk=pk)
    form = CourseForm(request.POST or None, instance=course)
    if form.is_valid():
        form.save()
        messages.success(request, "Course updated.")
        return redirect('course_list')
    return render(request, 'admins/course_form.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        messages.success(request, "Course deleted.")
        return redirect('course_list')
    return render(request, 'admins/course_confirm_delete.html', {'course': course})

# --- UNIT VIEWS ---

@login_required
@user_passes_test(is_admin)
def unit_list(request):
    units = Unit.objects.select_related('course').all()
    return render(request, 'admins/unit_list.html', {'units': units})

@login_required
@user_passes_test(is_admin)
def unit_create(request):
    form = UnitForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Unit created.")
        return redirect('unit_list')
    return render(request, 'admins/unit_form.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def unit_update(request, pk):
    unit = get_object_or_404(Unit, pk=pk)
    form = UnitForm(request.POST or None, instance=unit)
    if form.is_valid():
        form.save()
        messages.success(request, "Unit updated.")
        return redirect('unit_list')
    return render(request, 'admins/unit_form.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def unit_delete(request, pk):
    unit = get_object_or_404(Unit, pk=pk)
    if request.method == 'POST':
        unit.delete()
        messages.success(request, "Unit deleted.")
        return redirect('unit_list')
    return render(request, 'admins/unit_confirm_delete.html', {'unit': unit})

# --- NOTICE VIEWS ---

@login_required
@user_passes_test(is_admin)
def notice_list(request):
    notices = Notice.objects.all()
    return render(request, 'admins/notice_list.html', {'notices': notices})

@login_required
@user_passes_test(is_admin)
def notice_create(request):
    form = NoticeForm(request.POST or None)
    if form.is_valid():
        notice = form.save(commit=False)
        notice.posted_by = request.user.username
        notice.save()
        messages.success(request, "Notice posted.")
        return redirect('notice_list')
    return render(request, 'admins/notice_form.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def notice_update(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    form = NoticeForm(request.POST or None, instance=notice)
    if form.is_valid():
        form.save()
        messages.success(request, "Notice updated.")
        return redirect('notice_list')
    return render(request, 'admins/notice_form.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def notice_delete(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    if request.method == 'POST':
        notice.delete()
        messages.success(request, "Notice deleted.")
        return redirect('notice_list')
    return render(request, 'admins/notice_confirm_delete.html', {'notice': notice})

# --- EVENT VIEWS ---

@login_required
@user_passes_test(is_admin)
def event_list(request):
    events = Event.objects.all()
    return render(request, 'admins/event_list.html', {'events': events})

@login_required
@user_passes_test(is_admin)
def event_create(request):
    form = EventForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Event created.")
        return redirect('event_list')
    return render(request, 'admins/event_form.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def event_update(request, pk):
    event = get_object_or_404(Event, pk=pk)
    form = EventForm(request.POST or None, request.FILES or None, instance=event)
    if form.is_valid():
        form.save()
        messages.success(request, "Event updated.")
        return redirect('event_list')
    return render(request, 'admins/event_form.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        event.delete()
        messages.success(request, "Event deleted.")
        return redirect('event_list')
    return render(request, 'admins/event_confirm_delete.html', {'event': event})

# --- ADMIN PROFILE (Manage only your profile) ---

@login_required
@user_passes_test(is_admin)
def admin_profile_view(request):
    profile = get_object_or_404(AdminProfile, user=request.user)
    form = AdminProfileForm(request.POST or None, request.FILES or None, instance=profile)
    if form.is_valid():
        form.save()
        messages.success(request, "Profile updated.")
        return redirect('admin_profile')
    return render(request, 'admins/profile.html', {'form': form})

@login_required
def timetable_list(request):
    timetables = Timetable.objects.all()
    return render(request, 'admins/timetable_list.html', {'timetables': timetables})

@login_required
def timetable_create(request):
    if request.method == 'POST':
        form = TimetableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('timetable_list')
    else:
        form = TimetableForm()
    return render(request, 'admins/timetable_form.html', {'form': form})

@login_required
def timetable_update(request, pk):
    timetable = get_object_or_404(Timetable, pk=pk)
    if request.method == 'POST':
        form = TimetableForm(request.POST, instance=timetable)
        if form.is_valid():
            form.save()
            return redirect('timetable_list')
    else:
        form = TimetableForm(instance=timetable)
    return render(request, 'admins/timetable_form.html', {'form': form})

@login_required
def timetable_delete(request, pk):
    timetable = get_object_or_404(Timetable, pk=pk)
    if request.method == 'POST':
        timetable.delete()
        return redirect('timetable_list')
    return render(request, 'admins/timetable_delete_confirm.html', {'timetable': timetable})


def admin_list(request):
    admins = AdminProfile.objects.all()
    return render(request, 'admins/admin_list.html', {'admins': admins})

def admin_detail(request, pk):
    admin = get_object_or_404(AdminProfile, pk=pk)
    return render(request, 'admins/admin_detail.html', {'admin': admin})