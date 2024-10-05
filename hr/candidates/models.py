
from django.db import models


class Candidate(models.Model):
    firstName = models.CharField(max_length=50,blank=True)
    lastName = models.CharField(max_length=50,blank=True)
    email = models.EmailField(blank=True)
    phoneNumber = models.CharField(max_length=15,blank=True)
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    applyingFor = models.CharField(max_length=100,blank=True)  # Corresponds to `applyingFor`
    jobType = models.CharField(max_length=50,blank=True)  # New field for job type
    experience = models.CharField(max_length=50,blank=True)  # New field for experience
    currentCompany = models.CharField(max_length=100, blank=True)  # New field for current company
    currentLocation = models.CharField(max_length=100, blank=True)  # New field for current location
    date_applied = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"


class Admin(models.Model):
    user_name=models.CharField(max_length=50)
    password=models.CharField(max_length=30)