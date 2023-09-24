from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Job(models.Model):
    job_title = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    location = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    description = models.TextField()
    skills = models.TextField()
    salary = models.CharField(max_length=30)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.job_title
