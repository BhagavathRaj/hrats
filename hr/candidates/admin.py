from django.contrib import admin
from .models import Candidate
from .models import Admin
# Register your models here.

admin.site.register(Candidate)
admin.site.register(Admin)