from django.db import models
from django.contrib.auth.models import User
from admins.models import Course, Unit
# Create your models here.
class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reg_no = models.CharField(max_length=20, unique=True)
    unit = models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=15)
    profile_pic= models.ImageField(upload_to='student/', default='student/default.jpg', blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.reg_no}"



class Enrollment(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    Unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    class Meta:
        unique_together =('student','Unit')
    def __str__(self):
        return f"{self.student} - {self.Unit}"
    
class FeePayment(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=7, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=10)
    reference_number = models.CharField(max_length=20, unique=True)

class Grade(models.Model):
    enrollment = models.OneToOneField(Enrollment, on_delete=models.CASCADE)
    grade = models.CharField(max_length=2)
    marks = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return f"{self.enrollment} - {self.grade}"
    
class Timetable(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    day_of_the_week = models.CharField(max_length=10)
    start_time = models.TimeField()
    end_time = models.TimeField()
    venue = models.CharField(max_length=6) 

    def __str__(self):
        return f"{self.unit} - {self.day_of_the_week} - {self.start_time} - {self.end_time}"


        