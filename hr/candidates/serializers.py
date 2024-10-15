# serializers.py
from rest_framework import serializers
from .models import Candidate,InterviewApplication,ProgressStatus

class ProgressStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgressStatus
        fields = ['status', 'next_round', 'rejection_reason', 'updated_at']
class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = [
            'firstName',
            'lastName',
            'email',
            'phoneNumber',
            'resume',
            'applyingFor',
            'jobType',
            'experience',
            'currentCompany',
            'currentLocation',
           
        ] # Include all fields from the model
class InterviewApplicationSerializer(serializers.ModelSerializer):
    statuses = ProgressStatusSerializer(many=True, read_only=True)
    class Meta:
        model = InterviewApplication
        fields = [
            'name',  # Updated to match the new field name
            'role',  # Updated to match the new field name
            'phone_number',  # This field is retained as is
            'email_address',  # This field is retained as is
            'interview_date',  # This field is retained as is
            'interviewemail',  # Updated to match the new field name
            'interviewer_name',  # This field is retained as is
            'resume',  # This field is updated to be a URLField in the model
            'portfolio_link',  # This field is retained as is
            'statuses'
        ]

