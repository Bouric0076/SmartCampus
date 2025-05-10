from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reg_no = models.CharField(max_length=20 unique=True)
    year_of_study = models.PositiveIntegerField()
    Department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.user.username} - {self.reg_no}"



class Department(models.Model):
    name = models.CharField(max_length=100 unique=True)
    head_of_department = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name