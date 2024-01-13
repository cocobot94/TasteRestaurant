from django.forms.models import BaseModelForm
from django.shortcuts import render
from django.views.generic.edit import CreateView
from apps.users.models import User
from apps.users.forms import UserForm
from django import forms
from django.urls import reverse_lazy

# Create your views here.


class SignUpView(CreateView):
    form_class = UserForm
    template_name = "registration/signup.html"

    def get_success_url(self) -> str:
        return reverse_lazy("login") + "?register"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["username"].widget = forms.TextInput(
            attrs={"class": "form-control mb-2"}
        )
        form.fields["email"].widget = forms.EmailInput(
            attrs={"class": "form-control mb-2"}
        )
        form.fields["password1"].widget = forms.PasswordInput(
            attrs={"class": "form-control mb-2"}
        )
        form.fields["password2"].widget = forms.PasswordInput(
            attrs={"class": "form-control mb-2"}
        )
        return form
