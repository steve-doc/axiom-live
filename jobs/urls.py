from django.urls import path
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
    path('about/', views.about, name='jobs-about'),
    path('contact/', views.send_email, name='jobs-contact'),
]