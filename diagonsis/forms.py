from django import forms
from .models import MedicalTest

class MedicalTestForm(forms.ModelForm):
    class Meta:
        model = MedicalTest
        fields = ['image']
        labels = {'image': ''}
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'صورة الجلد'}),
        }
