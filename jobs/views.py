from django.shortcuts import render
from django.http import HttpResponse


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
    return render(request, 'jobs/home.html')


def postings(request):
    context = {
        'posts': posts
        }
    return render(request, 'jobs/postings.html', context)


def about(request):
    return render(request, 'jobs/about.html')
