from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms
from django.contrib.auth.forms import AuthenticationForm



class VerifyImageForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['verify_image']
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('first_name','last_name','email','age', 'is_doctor', 'is_admmin', 'is_user', 'image'
                                        ,'slug','address')

class AdminCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email', 'phone')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields

class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label='Email')