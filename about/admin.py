from django.contrib import admin
from .models import AboutMe
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(AboutMe)
class AboutMeAdmin(SummernoteModelAdmin):
    search_fields = ['content','title']
    summernote_fields = ('content',)