from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    search_fields = ['content','title']
    summernote_fields = ('content',)