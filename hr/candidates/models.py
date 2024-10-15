
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
    

class InterviewApplication(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    role = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    email_address = models.EmailField()
    
   
  
    interview_date = models.DateTimeField()
    interviewemail=  models.EmailField(null=True, blank=True)
    interviewer_name = models.CharField(max_length=100, null=True, blank=True)
  
    resume = models.URLField(null=True,blank=True)  # URLField to store the resume URL
    portfolio_link = models.URLField(null=True,blank=True)  # Field for the portfolio link
    

    def __str__(self):
        return f"{self.name} {self.role} - {self.interviewer_name}"
    
    def get_progress_status(self):
     "Retrieve all progress statuses for this interview application."
     statuses = self.statuses.all()
     print("Progress statuses:", statuses)
     return statuses

# class ProgressStatus(models.Model):
#     STATUS_CHOICES = [
#         ('application_received', 'Application Received'),
#             ('hr_interview', 'HR Interview'),
#             ('technical_interview', 'Technical Interview'),
#         ('selected', 'Selected'),
#         ('rejected', 'Rejected'),
#     ]

#     application = models.ForeignKey(InterviewApplication, on_delete=models.CASCADE, related_name='statuses')
#     status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='application_received')
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"{self.application.name} "
    
# Model to track the status and progress of candidates
class ProgressStatus(models.Model):
    STATUS_CHOICES = [
        ('application_received', 'Application Received'),
        ('move_to_next_round', 'Move To Next Round'),
        ('selected', 'Selected'),
        ('rejected', 'Rejected'),
    ]

    NEXT_ROUND_CHOICES = [
        ('hr_interview', 'HR Interview'),
        ('assessment', 'Assessment'),
        ('technical_interview', 'Technical Interview'),
    ]

    application = models.ForeignKey(InterviewApplication, on_delete=models.CASCADE, related_name='statuses')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    rejection_reason = models.TextField(null=True, blank=True)  # Can be null if not rejected
    next_round = models.CharField(max_length=50, choices=NEXT_ROUND_CHOICES, null=True, blank=True)  # Can be null for rejected/selected cases
    updated_at = models.DateTimeField(auto_now=True)  # Automatically updates on save

    def __str__(self):
        return f"{self.application.name} - {self.get_status_display()}"