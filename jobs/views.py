from django.shortcuts import render
from .models import Job


posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]



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
