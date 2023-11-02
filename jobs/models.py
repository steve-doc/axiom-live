from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Define presets for job type
JOB_TYPES = [
        ("Full-Time", "Full-Time"),
        ("Part-Time", "Part-Time"),
        ("Temp", "Temp"),
    ]


# Define job model
class Job(models.Model):
    job_title = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    location = models.CharField(max_length=30)
    job_type = models.CharField(max_length=15, choices=JOB_TYPES)
    description = models.TextField()
    skills = models.TextField()
    salary = models.CharField(max_length=30)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.job_title

    def get_absolute_url(self):
        return reverse('job-detail', kwargs={'pk': self.pk})
