from django.urls import path,include
from . import views
from django.contrib.auth.views import PasswordChangeView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', views.UserProfileListView.as_view(), name='index'),
    path('signup/', views.signUp, name='signup'),
    path('signup/successful',views.signupSuccessful , name='signup-successful'),
    path('profile/', views.UserProfileView.as_view(), name = 'profile'),
    path('profile/update/', views.UserProfileUpdate.as_view(), name = 'profile-update'),
    path('profile/update/profilephoto/', views.UserProfilePhotoUpdate.as_view(), name = 'profile-photo-update'),
    path('profile/password_change',PasswordChangeView.as_view(), name = 'password-change'),
]