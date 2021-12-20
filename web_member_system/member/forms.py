from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django import forms
from .models import UserProfile
# from django.utils.translation import ugettext_lazy as _
import datetime
import re

from django.forms.widgets import TextInput


class RegisterUserForm(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.CharField(max_length=100)
    password = forms.CharField(widget = forms.PasswordInput)
    
    def clean_username(self):
        username = self.cleaned_data['username']

        if len(username) < 6 :
            raise ValidationError("Input username is too short!")
        elif len(username) > 25:
            raise ValidationError("Input username is too long!")
        # do we allow same username?
        else :
            name_exist = User.objects.filter(username__exact = username)
            if len(name_exist):
                raise ValidationError("Username is already exist!")

        return username 
        
    def clean_email(self):
        email = self.cleaned_data['email']
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b' #refer from https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/
        
        if not re.match(regex,email):
            raise ValidationError("Invaild email format!")

        return email

    def clean_password(self):
        password = self.cleaned_data['password']

        if len(password) < 8:
            raise ValidationError("Password is too short!")
        elif len(password) > 25:
            raise ValidationError("Password is too long!")

        return password


# use forms.Form can custom form
# class UserProfileForm(forms.Form):
#     experience = forms.CharField(widget=forms.TextInput)
#     skill = forms.CharField(widget=forms.TextInput)
#     job = forms.CharField(widget=forms.TextInput)

#     cel = forms.CharField(max_length=100)
#     tel = forms.CharField(max_length=100)

#     def clean_experience(self):
#         experience = self.cleaned_data['experience']
#         return experience
    
#     def clean_skill(self):
#         skill = self.cleaned_data['skill']
#         return skill

#     def clean_job(self):
#         job = self.cleaned_data['job']
#         return job

#     def clean_cel(self):
#         cel = self.cleaned_data['cel']
#         return cel

#     def clean_tel(self):
#         tel = self.cleaned_data['tel']
#         return tel


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['experience','skill','job','cel','tel']

    def clean(self):
        for field, value in self.cleaned_data.items():
            self.cleaned_data[field] = value

class UserProfilePhotoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_photo',]
    
    def clean_profile_photo(self):
        profile_photo = self.cleaned_data['profile_photo']
        return profile_photo