from django.urls import path
from .views import CustomUserSignUpView,EmailLoginView,home,CustomeUserUpdateView,RateUpdateView,ChangePasswordView,overview,AdminsView,UsersView,DoctorsView,AddAdminCreateView,AdminUpdateView,VerifyDetail
app_name='accounts'
urlpatterns = [
    # account main 
    path("signup/", CustomUserSignUpView.as_view(), name="signup"),
    path("login/",EmailLoginView.as_view(),name="login"),
    path('',home,name='login_home' ),
    # Profile 
    path("profile/<str:slug>/",CustomeUserUpdateView.as_view(),name="profile"),
    path("profile/<str:slug>/feedback",RateUpdateView.as_view(),name="feedback"),
    path('profile/<str:slug>/change-password/', ChangePasswordView.as_view(), name='change_password'),
    path('doctor-certifcate/<str:slug>/', VerifyDetail.as_view(), name='verify'),
    
    # Admins 
    path('overview/',overview,name='overview' ),
    path('admins/', AdminsView.as_view(), name='admins'),
    path('users/', UsersView.as_view(), name='users'),
    path('doctors/', DoctorsView.as_view(), name='doctors'),
    path('add-admin/', AddAdminCreateView.as_view(), name='add_admin'),
    path("edit/<str:slug>/",AdminUpdateView.as_view(),name="edit"),
    
]