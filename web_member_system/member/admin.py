from django.contrib import admin
from .models import UserProfile
# Register your models here.

class UserProfileshow(admin.ModelAdmin):
    list_display = ('user','experience','skill','job', 'cel', 'tel', 'last_login_time')

admin.site.register(UserProfile, UserProfileshow)
