from django.contrib import admin
from .models import Contact
from .models import Experience
from .models import Project
from .models import Resume


# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile', 'message')


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title','company','start_date','end_date','description')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title','description','image','github_url')

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('uploaded_at',)