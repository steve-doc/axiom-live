from django.contrib import admin
from .models import Job
from django_summernote.admin import SummernoteModelAdmin


# Register Summernote in admin panel
@admin.register(Job)
class JobAdmin(SummernoteModelAdmin):

    summernote_fields = ('description', 'skills')
