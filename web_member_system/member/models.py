from django.contrib.auth.models import User,AbstractUser
from django.db import models
from django.urls import reverse

from datetime import datetime, timezone
import uuid

# Create your models here
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    experience = models.TextField(max_length=2000, null=True)
    skill = models.TextField(max_length=2000, null=True)
    job = models.TextField(max_length=2000, null=True)

    cel = models.CharField(max_length=100, null=True)
    tel = models.CharField(max_length=100, null=True)

    head_shot = models.CharField(max_length=100, default="template_of_head_shot.png")
    member_level = models.DecimalField(max_digits=10, decimal_places = 0, default=1)
    member_exp = models.DecimalField(max_digits=10, decimal_places = 0, default=0)

    last_login_time = models.DateField(null=True)
    # profile_photo = models.ImageField(upload_to='',null=True)

    
    def __str__(self):
        return self.user.__str__()
        # return self.skill

class UserProfileCard(models.Model):
    pass
    # user_profile = models.OneToOneField(UserProfile,on_delete=models.CASCADE, null=True)
    
    # def __str__(self):
    #     return self.user_profile.user.__str__()


