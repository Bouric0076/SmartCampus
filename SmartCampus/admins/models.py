from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(max_length=100, unique=True)
    head_of_department = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name
    
class Unit(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    unit_code =models.CharField(max_length=10, unique=True)
    lecture_hours =models.IntegerField()

    def __str__(self):
        return f"{self.unit_code} _ {self.name}"

class Notice(models.Model):
    title = models.CharField(max_length=200)
    date_posted = models.DateTimeField(auto_now_add=True)
    posted_by = models.CharField(max_length=20)
    content = models.TextField()
    
    def __str__(self):
        return self.title
    
class Event(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField() 
    time  = models.TimeField
    venue = models.CharField(max_length=20)
    image = models.ImageField(upload_to='events/', blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class AdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    profile_pic= models.ImageField(upload_to='admin/', default='admin/default.jpg', blank=True, null=True)
    is_staff = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.phone_number}"