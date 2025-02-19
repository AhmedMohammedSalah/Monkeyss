from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView #, UpdateView, DeleteView
from .forms import MedicalTestForm
from django.urls import reverse_lazy, reverse
from .models import MedicalTest
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .machine_code  import update_result 
from django.views.generic import DetailView
# Create your views here.

class TestCreateView(UserPassesTestMixin, LoginRequiredMixin, CreateView):
    model = MedicalTest
    template_name = "diagnosis.html"
    form_class = MedicalTestForm
    def get_success_url(self):
        return reverse('diagonsis:test_detail', kwargs={'pk': self.object.pk})
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['image'].widget.attrs['class'] = "form-control gh"
        form.fields['image'].widget.attrs['placeholder'] = "صورة الجلد "
        form.fields['image'].label = ""
        return form

    def form_valid(self, form):
        form.instance.user = self.request.user
        response= super().form_valid(form)
        update_result(self.object)
        return response
        
    
    def test_func(self):
        return self.request.user.is_user or self.request.user.is_doctor
# def post(self, request, *args, **kwargs):
#     form = self.get_form()
#     if form.is_valid():
#         instance = form.save(commit=False)
#         instance.image = request.FILES['image']
#         instance.save()
#         return self.form_valid(form)
#     else:
#         return self.form_invalid(form)

class MedicalTestDetailView(DetailView):
    model = MedicalTest
    template_name = 'result.html'
    context_object_name = 'test'
