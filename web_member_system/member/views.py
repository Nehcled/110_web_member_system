from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.signals import user_logged_in
from django.http import HttpResponseRedirect, request
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import UserProfile, UserProfileCard
from .forms import RegisterUserForm, UserProfileForm

from datetime import timezone, datetime
import os
from PIL import Image, ImageDraw, ImageFont
from re import template

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


def profileUpdate():
    pass

def logout():
    pass


CURRENT_DIRRECT = os.path.dirname(os.path.abspath(__file__))
class Card:
    def __init__(self, sender, user, request, **kwargs):
        self.user = user.get_username()
        self.id = user.id
        self.head_shot_path = user.userprofile.head_shot
        #self.exp = user.expiration_date
        self.exp = "21/12/19"  # Need to add "expiration date" in database.
        self.img = ""
        self.create_image()
        self.create_pdf()

    def create_image(self):
        def generate_font_family(font_family, size):
            return ImageFont.truetype(FONT_FAMILY_PATH[font_family], size=size, encoding="utf-8")

        def draw_text(draw, pos, text, font_size, font_family="Microsoft JhengHei Bold", font_color='rgb(0, 0, 0)'):
            draw.text(pos, text, fill=font_color, font=generate_font_family(font_family, font_size))

        FONT_FAMILY_PATH = {
            "Microsoft JhengHei Bold" : f"{CURRENT_DIRRECT}/static/font_family/Microsoft JhengHei/msjhbd.ttf",
        }
        self.img = Image.open(f"{CURRENT_DIRRECT}/static/pdf_profile/template.png")
        head_shot = Image.open(f"{CURRENT_DIRRECT}/static/head_shot/{self.head_shot_path}").resize((155, 155), Image.ANTIALIAS)
        self.img.paste(head_shot, (50, 77))
        draw = ImageDraw.Draw(self.img)
        user_id = str(self.id).zfill(8)
        user_id = user_id[0:4] + " " + user_id[4:]

        draw_text(draw, (232, 103), self.user, 50)
        draw_text(draw, (232, 183), user_id, 35)
        draw_text(draw, (386, 266), self.exp, 20)

    def create_pdf(self):
        self.img.save(f"{CURRENT_DIRRECT}/static/pdf_profile/{self.user}.pdf")

user_logged_in.connect(Card)

def increaseExp(sender, user, request, **kwargs):
    def can_increase(t1, t2):
        t1_d = t1.strftime("%d")
        t2_d = t2.strftime("%d") if t2 != None else -1
        return t1_d!=t2_d
    last_login_time = user.userprofile.last_login_time
    now_time = user.last_login.utcnow().replace(tzinfo=timezone.utc).astimezone(tz=None)
    target = UserProfile.objects.filter(user=user.id)[0]
    if can_increase(now_time, last_login_time):
        target.member_exp += 1
        if target.member_exp >= 100:
            target.member_level += 1
        target.member_exp %= 100
    target.last_login_time = now_time
    target.save()

user_logged_in.connect(increaseExp)


# Not finished
class LevelReward:
    def __init__(self, level):
        self.LEVLE_NAME = ["Basic", "Intermediate", "Advanced"]
        self.level = self.get_level(level)
    def get_level(self, level):
        if 20 >= level >= 1:
            return self.LEVLE_NAME[0]
        if 40 >= level >= 21:
            return self.LEVLE_NAME[1]
        return self.LEVLE_NAME[2]
    def enable(self):
        pass
