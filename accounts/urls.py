from django.urls import path
from .views import CustomUserSignUpView,EmailLoginView,home,CustomeUserUpdateView,RateUpdateView,ChangePasswordView
app_name='accounts'
urlpatterns = [
    path("signup/", CustomUserSignUpView.as_view(), name="signup"),
    path("login/",EmailLoginView.as_view(),name="login"),
    path('',home,name='login_home' ),
    path("profile/<str:slug>/",CustomeUserUpdateView.as_view(),name="profile"),
    path("profile/<str:slug>/feedback",RateUpdateView.as_view(),name="feedback"),
    path('profile/<str:slug>/change-password/', ChangePasswordView.as_view(), name='change_password'),

]