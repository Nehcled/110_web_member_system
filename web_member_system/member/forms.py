from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.db import models
from django import forms
from .models import UserProfile
import datetime
import re


# we use user creation from django.contrib.auth.forms
class UserSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

    def clean_email(self):
        email = self.cleaned_data['email']
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b' #refer from https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/    
        if not re.match(regex,email):
            raise ValidationError("Invaild email format!")
        return email
   


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

