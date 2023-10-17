from django.contrib import admin
from .models import Job
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Job)
class JobAdmin(SummernoteModelAdmin):

    summernote_fields = ('description', 'skills')

# admin.site.register(Job) not required when using the above decorator