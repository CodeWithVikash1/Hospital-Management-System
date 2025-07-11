from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=20)
    contact = models.CharField(max_length=15)
    specialization = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending')
    
    def __str__(self):
        return f"Dr. {self.user.first_name} {self.user.last_name}"

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    contact = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField()
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Declined', 'Declined'),('Completed','Completed')], default='Pending')
    
    def __str__(self):
        return f"Dr. {self.doctor.user.first_name} {self.doctor.user.last_name} with {self.patient.user.first_name} {self.patient.user.last_name}"
    