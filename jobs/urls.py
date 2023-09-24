from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='jobs-home'),
    path('postings/', views.postings, name='jobs-postings'),
    path('about/', views.about, name='jobs-about'),
]