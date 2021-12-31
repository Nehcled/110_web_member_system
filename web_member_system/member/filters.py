import django_filters
from django import forms
from django.contrib.auth.models import User

class UserFilter(django_filters.FilterSet):
  username = django_filters.CharFilter(
      lookup_expr='icontains',
      widget=forms.TextInput(attrs={'class': 'form-control'}))
  userprofile__skill = django_filters.CharFilter(
      lookup_expr='icontains',
      widget=forms.TextInput(attrs={'class': 'form-control'}))
  userprofile__job = django_filters.CharFilter(
      lookup_expr='icontains',
      widget=forms.TextInput(attrs={'class': 'form-control'}))
  class Meta:
    model = User
    fields = ['username','userprofile__skill','userprofile__job']

