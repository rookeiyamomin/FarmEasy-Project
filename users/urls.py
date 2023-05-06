from django.urls import path
from users import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("register", views.register, name="register"),
    path('login',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout',auth_views.LogoutView.as_view(template_name='logout.html'),name='logout'),
    path("user_data", views.user_data, name="user_data"),
    path("farmer_crop_profile", views.farmer_crop_profile_view, name="farmer_crop_profile"),
    path("profile", views.profile, name="profile"),
]