from django.urls import path,include
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', views.UserProfileListView.as_view(), name='index'),
    path('register/', views.register, name='register'),
    path('register/successful',views.registerSuccessful , name='register-successful'),
    path('profile/', views.UserProfileView.as_view(), name = 'profile'),
    path('profile/update/', views.UserProfileUpdate.as_view(), name = 'profile-update'),
    path('profile/update/profilephoto/', views.UserProfilePhotoUpdate.as_view(), name = 'profile-photo-update'),
]