from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login as auth_login
from django.views.generic import CreateView,UpdateView
from .forms import CustomUserCreationForm,EmailAuthenticationForm
from .models import CustomUser
from django.contrib.auth.decorators import login_required# Create your views here.


class CustomUserSignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("accounts:login")
    template_name = "registration/signup.html"
    def get_form(self, form_class=None):
        form = super().get_form(form_class) 
        form.fields['first_name'].widget.attrs['class'] = "input"
        form.fields['first_name'].label = ""
        form.fields['first_name'].help_text = ""         
        form.fields['last_name'].widget.attrs['class'] = "input"
        form.fields['last_name'].label = ""
        form.fields['last_name'].help_text = "" 
        form.fields['email'].widget.attrs['class'] = "input"
        form.fields['email'].label = ""
        form.fields['email'].help_text = "" 
        
        form.fields['address'].widget.attrs['class'] = "input"
        form.fields['address'].label = ""
        form.fields['address'].help_text = "" 
        
        
        form.fields['password1'].widget.attrs['class'] = "input"
        form.fields['password1'].label = ""
        form.fields['password1'].help_text = "" 
        
        
        form.fields['password2'].widget.attrs['class'] = "input"
        form.fields['password2'].label = ""
        form.fields['password2'].help_text = "" 
        
        form.fields['age'].widget.attrs['class'] = "input"
        form.fields['age'].label = ""
        form.fields['age'].help_text = "" 
        
        form.fields['image'].widget.attrs['class'] = "input"
        form.fields['image'].label = ""
        form.fields['image'].help_text = "" 
        
        form.fields['is_user'].widget.attrs['class'] = "input"
        form.fields['is_user'].label = "User"
        form.fields['is_user'].help_text = "" 
        
        form.fields['is_doctor'].widget.attrs['class'] = "input"
        form.fields['is_doctor'].label = "Doctor"
        form.fields['is_doctor'].help_text = "" 
        
        form.fields['is_admmin'].widget.attrs['class'] = "input"
        form.fields['is_admmin'].label = "Admin"
        form.fields['is_admmin'].help_text = "" 
        
        return form

class EmailLoginView(LoginView):
    form_class = EmailAuthenticationForm
    template_name = 'registration/login.html'
    def get_form(self, form_class=None):
        form = super().get_form(form_class) 
        form.fields['username'].widget.attrs['class'] = "input"
        form.fields['username'].label = ""
        form.fields['username'].help_text = "" 
        form.fields['password'].widget.attrs['class'] = "input"
        form.fields['password'].label = ""
        form.fields['password'].help_text = ""
        return form
    
@login_required
def home(request):
    if request.user.is_user:
        context = {}
        return render(request, 'roles/userhome.html', context)
    elif request.user.is_admmin:
        context = {}
        return render(request, 'roles/dashboard-overview.html', context)
    elif request.user.is_doctor:
        context = {}
        return render(request, 'roles/doctorhome.html', context)
    else:
        return redirect(reverse('login'))




class CustomeUserUpdateView(UpdateView):
    model = CustomUser
    template_name = "roles/user_settings.html"
    fields = ['first_name', 'last_name', 'email','age','address']
    def get_success_url(self):
        return reverse('accounts:profile', kwargs={'slug': self.request.user.slug})
class RateUpdateView(UpdateView):
    model = CustomUser
    template_name = "roles/user-feedback.html"
    fields = ['rate1','rate4','rate2','rate3','rate5',]
    def get_success_url(self):
        return reverse('accounts:feedback', kwargs={'slug': self.request.user.slug})
    def form_valid(self, form):
        if form.instance.rate2:
            form.instance.rate1=True
        if form.instance.rate3:
            form.instance.rate1=True
            form.instance.rate2=True        
        if form.instance.rate4:
            form.instance.rate1=True
            form.instance.rate2=True
            form.instance.rate3=True        
        if form.instance.rate5:
            form.instance.rate1=True
            form.instance.rate2=True
            form.instance.rate3=True
            form.instance.rate4=True
        return super().form_valid(form)
    
from django.contrib.auth.forms import PasswordChangeForm

class CustomChangePasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs['class'] = 'password'
        self.fields['old_password'].label = ''
        self.fields['old_password'].help_text = ''
        self.fields['new_password1'].widget.attrs['class'] = 'password'
        self.fields['new_password1'].label = ''
        self.fields['new_password1'].help_text = ''
        self.fields['new_password2'].widget.attrs['class'] = 'password'
        self.fields['new_password2'].label = ''
        self.fields['new_password2'].help_text = ''

class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'roles/change_password.html'
    success_url = reverse_lazy('accounts:profile') 
    success_message = "Your password has been changed successfully."
    form_class = CustomChangePasswordForm