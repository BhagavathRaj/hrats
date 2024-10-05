# serializers.py
from rest_framework import serializers
from .models import Candidate

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
