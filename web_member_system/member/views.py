from re import template
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from .models import UserProfile, UserProfileCard
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .forms import RegisterUserForm, UserProfileForm
from django.http import HttpResponseRedirect, request
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.class
def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            
            user = User.objects.create_user(username = username, password = password, email = email)

            userprofile = UserProfile(user = user)
            userprofile.save()

            return HttpResponseRedirect(reverse('register-successful'))
    else:
        form = RegisterUserForm()
    
    return render(request, 'member/register_member_account.html', {'form': form })


def registerSuccessful(request):
    return render (request, 'member/register_successful.html')

class test(CreateView):
    model = User

class UserProfileListView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'userprofile_list'
    model = User

class UserProfileView(LoginRequiredMixin,generic.DetailView):
    template_name = 'member/profile.html'
    context_object_name = 'profile'
    model = User

    def get_object(self):
        return self.request.user
class UserProfileUpdate(UpdateView):
    model = UserProfile
    template_name = 'member/profile_update.html'
    
    fields = ['experience','skill','job','cel','tel']

    success_url = reverse_lazy('profile')
    def get_object(self):
        return self.request.user.userprofile

# def updateProfile(request):
#     if request.method == 'POST':
#         form = UserProfileForm(request.POST)
#         if form.is_valid():
#             experience = form.cleaned_data['experience']
#             skill = form.cleaned_data['skill']
#             job = form.cleaned_data['job']
#             cel = form.cleaned_data['cel']
#             tel = form.cleaned_data['tel']


