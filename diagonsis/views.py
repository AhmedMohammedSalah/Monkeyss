from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView #, UpdateView, DeleteView
from .forms import MedicalTestForm
from django.urls import reverse_lazy, reverse
from .models import MedicalTest
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from machine_result import update_result
# Create your views here.

class TestCreateView(UserPassesTestMixin, LoginRequiredMixin, CreateView):
    model = MedicalTest
    template_name = "diagnosis.html"
    form_class = MedicalTestForm
    success_url = reverse_lazy('accounts:login_home')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['image'].widget.attrs['class'] = "form-control"
        form.fields['image'].widget.attrs['placeholder'] = "صورة الجلد "
        form.fields['image'].label = ""
        return form

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

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