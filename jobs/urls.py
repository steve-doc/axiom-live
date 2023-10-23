from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import (
    JobListView,
    JobDetailView,
    JobCreateView,
    JobUpdateView,
    JobDeleteView,
    send_email,)


urlpatterns = [
    path('', views.home, name='jobs-home'),
    path('postings/', JobListView.as_view(), name='jobs-postings'),
    path('job/<int:pk>/', JobDetailView.as_view(), name='job-detail'),
    path('job/<int:pk>/update/', JobUpdateView.as_view(), name='job-update'),
    path('job/<int:pk>/delete/', JobDeleteView.as_view(), name='job-delete'),
    path('job/new/', JobCreateView.as_view(), name='job-create'),
    path('services/', views.services, name='jobs-services'),
    path('contact/', views.send_email, name='jobs-contact'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)