# views.py
import json 
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Candidate
from .serializers import CandidateSerializer
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Admin
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

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password
import json
from .models import Admin

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Admin  # Import your Admin model
from django.contrib.auth.hashers import check_password  # For password verification

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

     