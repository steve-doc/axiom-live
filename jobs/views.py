from django.shortcuts import render
from .models import Job



def home(request):
    return render(request, 'jobs/home.html', {'title': 'Home'})


def postings(request):
    context = {
		'jobs': Job.objects.all()
    }
    return render(request, 'jobs/postings.html', context)


def about(request):
    return render(request, 'jobs/about.html', {'title': 'About'})


def contact(request):
    return render(request, 'jobs/contact.html', {'title': 'Contact'})
