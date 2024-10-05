# urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import create_candidate,get_candidates,home
from .views import admin_login_api
urlpatterns = [
    path('', home, name='home'),
    path('create-candidate/', create_candidate, name='create-candidate'),
    path('get-candidates/', get_candidates, name='get-candidates'),# URL for posting candidate details
    path('api/admin/login/', admin_login_api, name='admin_login_api'), 
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
