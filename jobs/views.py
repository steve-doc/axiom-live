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