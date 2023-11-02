from django import forms
from .models import Job
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


# Create job update form and implement summernote
class JobUpdateForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = [
            'job_title',
            'date_posted',
            'location',
            'job_type',
            'description',
            'skills',
            'salary']
        widgets = {
            'description': SummernoteWidget(),
            'skills': SummernoteWidget()
        }
