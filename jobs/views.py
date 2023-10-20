from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Job
from django.core.mail import EmailMessage, get_connection
from django.conf import settings




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


class JobListView(ListView):
    model = Job
    template_name = 'jobs/postings.html'
    context_object_name = 'jobs'
    ordering = ['-date_posted']
    paginate_by = 5


class JobDetailView(DetailView):
    model = Job
    fields = [
        'job_title',
        'location',
        'job_type',
        'description',
        'skills',
        'salary'
        ]


class JobCreateView(LoginRequiredMixin, CreateView):
    model = Job
    fields = [
        'job_title',
        'location',
        'job_type',
        'description',
        'skills',
        'salary'
        ]
    
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class JobUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Job
    fields = [
        'job_title',
        'location',
        'job_type',
        'description',
        'skills',
        'salary'
        ]
    
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    def test_func(self):
        job = self.get_object()
        if self.request.user == job.creator:
            return True
        return False


class JobDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Job
    success_url = "/postings/"
  
    def test_func(self):
        job = self.get_object()
        if self.request.user == job.creator:
            return True
        return False


def send_email(request):
    if request.method == "POST":
        with get_connection(
            host=settings.EMAIL_HOST,
            port=settings.EMAIL_PORT,
            username=settings.EMAIL_HOST_USER,
            password=settings.EMAIL_HOST_PASSWORD,
            use_tls=settings.EMAIL_USE_TLS
        ) as connection:    
            email_from = settings.EMAIL_HOST_USER
            name = request.POST.get("name")
            recipient_list = [request.POST.get("email"), ] 
            tel = request.POST.get("tel")
            message = request.POST.get("message")
            EmailMessage(email_from, name, recipient_list, tel, message, connection=connection).send()

    return render(request, 'jobs/contact.html', {'title': 'Contact'})
