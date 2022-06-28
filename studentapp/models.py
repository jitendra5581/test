import email
from email.mime import application
from django.db import models

# Create your models here.

class StdentDetails(models.Model):
    rollno = models.IntegerField()
    name = models.CharField(max_length=50, null=True)
    marks = models.IntegerField()
    description = models.TextField(null=True)
    email = models.EmailField(null=True)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


class AdmissionDetails(models.Model):
    application_no = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50)
    section = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class RollnoDetails(models.Model):
    rollno = models.IntegerField(primary_key=True)
    app_no = models.ForeignKey(AdmissionDetails, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.rollno)