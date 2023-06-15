from django.contrib import admin
from api.models import Profile

@admin.register(Profile)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'dob' ,'state', 'gender', 'location', 'pimage', 'rdoc', 'phone', 'address', 'summary', 'skills', 'experience', 'education', 'projects', 'achievements', 'hobbies']

