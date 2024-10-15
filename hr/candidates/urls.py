# urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import create_candidate,get_candidates,home
from .views import admin_login_api,submit_application,ApplicationStatusView,ProgressStatusViewSet,InterviewApplicationListCreateView
urlpatterns = [
    path('', home, name='home'),
    path('create-candidate/', create_candidate, name='create-candidate'),
    path('get-candidates/', get_candidates, name='get-candidates'),# URL for posting candidate details
    path('api/admin/login/', admin_login_api, name='admin_login_api'), 
    path('submit/', submit_application.as_view(), name='submit-application'),
    path('applications/', InterviewApplicationListCreateView.as_view(), name='interview-application-list'),
    path('interviewstatus/<str:application_name>/',ApplicationStatusView.as_view(),name='application-status'),
    path('progressstatus/update/<str:application_name>/', ProgressStatusViewSet.as_view({'post': 'update_status'}), name='update-progress-status')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

