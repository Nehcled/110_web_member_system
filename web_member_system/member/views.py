from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.signals import user_logged_in
from django.db.models.query import QuerySet
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, request
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from .models import UserProfile
from .forms import UserSignUpForm, UserProfileForm, UserProfilePhotoForm
from datetime import timezone, datetime
import os
from PIL import Image, ImageDraw, ImageFont


from .filters import UserFilter
from django.contrib import messages
# Create your views here.class
def signUp(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            
            user = User.objects.create_user(username = username, password = password, email = email)

            userprofile = UserProfile(user = user)
            userprofile.save()

            return HttpResponseRedirect(reverse('signup-successful'))
    else:
        form = UserSignUpForm()
    
    return render(request, 'member/signup_member_account.html', {'form': form })

def signupSuccessful(request):
    return render (request, 'member/signup_successful.html')

# for index.html
class UserProfileListView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'userprofile_list'
    model = User


class UserProfileView(LoginRequiredMixin, generic.DetailView):
    template_name = 'member/profile.html'
    context_object_name = 'profile'
    model = User

    def get_object(self):
        return self.request.user

class UserProfileUpdate(UpdateView):
    model = UserProfile

    # use custom form to clean the data
    form_class = UserProfileForm
    template_name = 'member/profile_update.html'
    
    # use fields to auto generate form
    # fields = ['experience','skill','job','cel','tel']

    success_url = reverse_lazy('profile')
    def get_object(self):
        return self.request.user.userprofile

class UserProfilePhotoUpdate(UpdateView):
    model = UserProfile
    form_class = UserProfilePhotoForm
    template_name = 'member/profile_photo_update.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user.userprofile

# class UserPasswordVerify(FormView):
#     form_class = UserPasswordVerifyForm
#     template_name = 'member/profile.html'

#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         kwargs.update(request = self.request)
#         return kwargs

#     def get_success_url(self):
#         return reverse_lazy('profile')

    
    


CURRENT_DIRRECT = os.path.dirname(os.path.abspath(__file__))

class Card:
    def __init__(self, sender, user, request, **kwargs):
        self.user = user.get_username()
        self.id = user.id
        self.headShotPath = user.userprofile.head_shot
        #self.exp = user.expiration_date
        self.exp = "25/01/01"  # Need to add "expiration date" in database.
        self.img = ""
        self.createImage()
        self.createPdf()

    def createImage(self):
        def generateFontFamily(font_family, size):
            return ImageFont.truetype(FONT_FAMILY_PATH[font_family], size=size, encoding="utf-8")

        def drawText(draw, pos, text, font_size, font_family="Microsoft JhengHei Bold", font_color='rgb(0, 0, 0)'):
            draw.text(pos, text, fill=font_color, font=generateFontFamily(font_family, font_size))

        FONT_FAMILY_PATH = {
            "Microsoft JhengHei Bold" : f"{CURRENT_DIRRECT}/static/font_family/Microsoft JhengHei/msjhbd.ttf",
        }
        self.img = Image.open(f"{CURRENT_DIRRECT}/static/pdf_profile/template.png")
        head_shot = Image.open(f"{CURRENT_DIRRECT}/static/head_shot/{self.headShotPath}").resize((155, 155), Image.ANTIALIAS)
        self.img.paste(head_shot, (50, 77))
        draw = ImageDraw.Draw(self.img)
        user_id = str(self.id).zfill(8)
        user_id = user_id[0:4] + " " + user_id[4:]

        drawText(draw, (232, 103), self.user, 50)
        drawText(draw, (232, 183), user_id, 35)
        drawText(draw, (386, 266), self.exp, 20)

    def createPdf(self):
        self.img.save(f"{CURRENT_DIRRECT}/static/pdf_profile/{self.user}.pdf")

user_logged_in.connect(Card)

def increaseExp(sender, user, request, **kwargs):
    def sameDay(t1, t2):
        day1 = t1.strftime("%d")
        day2 = t2.strftime("%d") if t2 != None else -1
        return day1 == day2
    lastLoginTime = user.userprofile.last_login_time
    nowTime = user.last_login.utcnow().replace(tzinfo=timezone.utc).astimezone(tz=None)
    target = UserProfile.objects.filter(user=user.id)[0]
    if not sameDay(nowTime, lastLoginTime):
        target.member_exp += 35
        target.member_level += target.member_exp // 100
        target.member_exp %= 100
    target.last_login_time = nowTime
    target.save()

user_logged_in.connect(increaseExp)



def index_search(request):
    user = User.objects.all()
    userFilter = UserFilter(queryset=user)
    if request.method == "POST":
        userFilter = UserFilter(request.POST, queryset=user)

    context = {
        'userFilter' : userFilter
    }
    return render(request, 'search.html', context)

