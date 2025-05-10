from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import StudentProfile, Enrollment, FeePayment, Grade, Timetable


# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        reg_no = request.POST['reg_no']
        date_of_birth = request.POST['date_of_birth']
        phone_number = request.POST['phone_number']
        # course_id = request.POST['Course']

        if User.objects.filter(username=username).exists():
            # Handle duplicate username
            messages.error(request, 'Username already exists.')
            # maybe redirect back to registration form
        else:
            # Create the user
            user = User.objects.create_user(username=username, password=password)
        course = course.objects.get(id=course_id)
        student_profile = StudentProfile.objects.create(user=user, reg_no=reg_no, date_of_birth=date_of_birth, phone_number=phone_number, course=course)

        return redirect('login')
    else:
        return render(request, 'students/register.html')
    

@login_required
def profile(request):
    student_profile = StudentProfile.objects.get(user=request.user)
    return render(request, 'students/profile.html', {'student_profile': student_profile})

@login_required
def dashboard(request):
    if request.user.is_staff:
        return redirect('/admin/dashboard')
    else:
        student_profile = StudentProfile.objects.get(user=request.user)
        enrollments = Enrollment.objects.filter(student=student_profile)
        fee_payments = FeePayment.objects.filter(student=student_profile)
        grades = Grade.objects.filter(enrollment__student=student_profile)
        timetable = Timetable.objects.filter(unit__in=enrollments.values('unit'))

        return render(request, 'students/dashboard.html', {
            'student_profile': student_profile,
            'enrollments': enrollments,
            'fee_payments': fee_payments,
            'grades': grades,
            'timetable': timetable,
        })
    
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # redirect to a success page
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'students/login.html')