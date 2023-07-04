from django import forms
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    PasswordResetForm,
)

from project.apps.users.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    # def clean(self):
    #     cleaned_data = super().clean()
    #     password1 = cleaned_data.get("password1")
    #     password2 = cleaned_data.get("password2")
    #     if password1 and password2 and password1 != password2:
    #         raise forms.ValidationError("Passwords do not match2")

    #     if len(password1) < 8:
    #         raise forms.ValidationError(
    #             "Password should be at least 81 characters long"
    #         )

    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "phone",
            "password1",
            "password2",
        )
        widgets = {
            "username": TextInput(
                attrs={
                    "class": "form-control radius-30 ps-5",
                    "id": "inputName",
                    "placeholder": "Enter your name",
                }
            ),
            "email": EmailInput(
                attrs={
                    "class": "form-control radius-30 ps-5",
                    "id": "inputEmailAddress",
                    "placeholder": "Enter your email",
                }
            ),
            "phone": TextInput(
                attrs={
                    "class": "form-control radius-30 ps-5",
                    "id": "inputName",
                    "placeholder": "Enter your phone",
                }
            ),
            "password1": TextInput(
                attrs={
                    "class": "form-control radius-30 ps-5",
                    "id": "inputChoosePassword1",
                    "placeholder": "Enter your password",
                }
            ),
            "password2": TextInput(
                attrs={
                    "class": "form-control radius-30 ps-5",
                    "id": "inputChoosePassword2",
                    "placeholder": "Enter your password",
                }
            ),
        }


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "password")


class CustomPasswordResetForm(PasswordResetForm):
    class Meta:
        model = CustomUser
        fields = ("email", "phone")


class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone",
            "street_address_1",
            "street_address_2",
            "city",
            "bio",
            "instagram_link",
            "telegram_link",
        ]