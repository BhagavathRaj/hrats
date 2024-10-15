# views.py
import json 
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Candidate,ProgressStatus
from .serializers import CandidateSerializer,InterviewApplicationSerializer,ProgressStatusSerializer
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Admin,InterviewApplication
from django.core.mail import EmailMessage
from django.conf import settings
from rest_framework import generics
from rest_framework import status

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password
import json
from .models import Admin
from rest_framework.views import APIView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Admin  # Import your Admin model
from django.contrib.auth.hashers import check_password  # For password verification
from rest_framework import viewsets
@api_view(['POST'])
def create_candidate(request):
    print("Request body:", request.body)  # Log the raw request body
    print("Request content type:", request.content_type)  # Log the content type
    print("Received data:", request.data)  # Log the received data
    
    if request.method == 'POST':
        # Initialize the serializer with the incoming data
        serializer = CandidateSerializer(data=request.data)
        
        # Check if the provided data is valid
        if serializer.is_valid():
            serializer.save()  # Save the candidate instance
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # If the data is not valid, return the errors
        print("Validation errors:", serializer.errors)  # Print validation errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def get_candidates(request):
    if request.method == 'GET':
        candidates = Candidate.objects.all()  # Retrieve all candidate records
        serializer = CandidateSerializer(candidates, many=True)  # Serialize the data
        return Response(serializer.data, status=status.HTTP_200_OK)

def home(request):
    # return Response({"message":"welcome to ats","status":200})
    return render( request,'home.html')


# from django.views.decorators.csrf import csrf_exempt
# from django.http import JsonResponse
# import json
# from .models import Admin

# @csrf_exempt
# def admin_login_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_name = data.get('user_name')
        password = data.get('password')
        # print(  user_name = data.get('user_name'))
        # print(  user_name = data.get('password'))

        try:
            # Check if admin exists
            admin = Admin.objects.get(user_name=user_name, password=password)
            
            # Return more useful data, such as admin details
            return JsonResponse({
                'success': True,
                'message': 'Login successful',
                'admin': {
                    'id': admin.id,
                    'user_name': admin.user_name,
                    # Add any other fields you wish to return
                }
            })
        except Admin.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Invalid credentials'})

    return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=400)

@csrf_exempt
def admin_login_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_name = data.get('user_name')
            password = data.get('password')

            print("Received user_name:", user_name)
            print("Received password:", password)

            print("hello login.....")
            admin = Admin.objects.get(user_name=user_name)
            print("Admin found:", admin.user_name)

            # Check if the provided password matches the stored hashed password
            if password == admin.password: # Assuming passwords are hashed
                return JsonResponse({
                    'success': True,
                    'message': 'Login successful',  # Success message
                    'admin': {
                        'id': admin.id,
                        'user_name': admin.user_name,
                        # Add any other fields you wish to return
                    }
                })
            else:
                return JsonResponse({'success': False, 'message': 'Invalid credentials'})

        except Admin.DoesNotExist:
            print("Admin does not exist")
            return JsonResponse({'success': False, 'message': 'Invalid credentials'})

    return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=400)

# @api_view(['POST'])
# def submit_application(request):
#     if request.method == 'POST':
#         serializer = InterviewApplicationSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             # Here, you can send the email with the resume
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
from rest_framework import generics
from django.core.mail import EmailMessage
from django.conf import settings
from .models import InterviewApplication, ProgressStatus
from .serializers import InterviewApplicationSerializer


        
class submit_application(generics.CreateAPIView):
    queryset = InterviewApplication.objects.all()
    serializer_class = InterviewApplicationSerializer

    def perform_create(self, serializer):
        # Save the InterviewApplication instance
        instance = serializer.save()

        # Create a progress status with the default status
        self.create_progress_status(instance)

        # Send email notification
        self.send_email(instance)

    def create_progress_status(self, application):
        # Create a new progress status record with the default status
        ProgressStatus.objects.create(application=application, status='application_received')

    def send_email(self, application):
        email = EmailMessage(
            subject='New Job Application',
            body=f'You have a new job application from {application.name} for the role of  {application.role}.',
            from_email=settings.EMAIL_HOST_USER,
            to=[application.interviewemail, application.email_address],   # Change to your recipient's email
        )
        print(application.interviewemail)
        print(application. email_address)
        # print("DS",application.email)
        # Check if the candidate has a resume and attach it
        if application.resume:
         email.body += f'\n\nResume Link: {application.resume}'  # Append the resume link to the email body
        else:
         print("No resume URL provided for the application.")  # Optional log

        email.send()

# class ProgressStatusViewSet(viewsets.ModelViewSet):
#     queryset = ProgressStatus.objects.all()
#     serializer_class = ProgressStatusSerializer

#     def update_status(self, request, application_name):
#         # Try to get the InterviewApplication instance by name
#         try:
#             application = InterviewApplication.objects.get(name=application_name)
#         except InterviewApplication.DoesNotExist:
#             return Response({"error": "Application not found"}, status=status.HTTP_404_NOT_FOUND)

#         # Extract status from request data
#         status_input = request.data.get('status')
#         next_round = request.data.get('nextRound')
#         rejection_reason = request.data.get('rejectionReason')
#         print(status_input)
#         print(next_round)
#         print(rejection_reason)
#         # Check if the status is valid according to STATUS_CHOICES
#         if status_input  in dict(ProgressStatus.STATUS_CHOICES):
#             return Response({"error": "Invalid status"}, status=status.HTTP_400_BAD_REQUEST)

#         # Update or create ProgressStatus instance for the application
#         progress_status, created = ProgressStatus.objects.update_or_create(
#             application=application,
#             defaults={
#                 'status': status_input,
#                 'next_round': next_round if status_input == 'move_to_next_round' else None,
#                 'rejection_reason': rejection_reason if status_input == 'rejected' else None,
#             }
#         )

#         # Return updated progress status
#         serializer = ProgressStatusSerializer(progress_status)
#         return Response(serializer.data, status=status.HTTP_200_OK)

    

class ApplicationStatusView(APIView):
    def get(self, request, application_name):
        print("*****", application_name)
        try:
            # Use filter() to get all matching applications
            applications = InterviewApplication.objects.filter(name=application_name)
            
            if not applications.exists():
                return Response({"error": "Application not found"}, status=404)
            
            # If multiple applications are found, return the most recent status for each
            statuses = []
            for application in applications:
                progress_status = application.statuses.order_by('-updated_at').first()
                statuses.append({
                    'application': str(application),
                    'status': str(progress_status.status),
                    'last_updated': progress_status.updated_at
                })
            
            return Response(statuses)

        except Exception as e:
            return Response({"error": str(e)}, status=500)
class InterviewApplicationListCreateView(generics.ListCreateAPIView):
    queryset = InterviewApplication.objects.all()
    serializer_class = InterviewApplicationSerializer

class ProgressStatusViewSet(viewsets.ModelViewSet):
    queryset = ProgressStatus.objects.all()
    serializer_class = ProgressStatusSerializer

    def update_status(self, request, application_name):
        # Try to get the InterviewApplication instance by name
        try:
            application = InterviewApplication.objects.get(name=application_name)
        except InterviewApplication.DoesNotExist:
            return Response({"error": "Application not found"}, status=status.HTTP_404_NOT_FOUND)

        # Extract status from request data
        status_input = request.data.get('status')
        next_round = request.data.get('nextRound')
        rejection_reason = request.data.get('rejectionReason')

        # Print values for debugging
        print(f"Status Input: {status_input}")
        print(f"Next Round: {next_round}")
        print(f"Rejection Reason: {rejection_reason}")

        # Check if the status is valid according to STATUS_CHOICES
        # valid_statuses = [choice[0] for choice in ProgressStatus.STATUS_CHOICES]
        # if status_input not in valid_statuses:
        #     return Response({"error": "Invalid status"}, status=status.HTTP_400_BAD_REQUEST)

        # Prepare the defaults for the update or create
        defaults = {
            'status': status_input,
            'next_round': next_round if status_input == 'Move To Next Round' else None,
            'rejection_reason': rejection_reason if status_input == 'Rejected' else None,
        }

        # Debug: Check what will be saved
        print(f"Defaults to be saved: {defaults}")

        # Update or create ProgressStatus instance for the application
        progress_status, created = ProgressStatus.objects.update_or_create(
            application=application,
            defaults=defaults
        )

        # Return updated progress status
        serializer = ProgressStatusSerializer(progress_status)
        return Response(serializer.data, status=status.HTTP_200_OK)
