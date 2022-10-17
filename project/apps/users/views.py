from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import PermissionDenied
from django.forms import ValidationError
from django.shortcuts import render, redirect, reverse

from django.views import View


class RegisterView(View):
    def get(self, request):
        return render(request, "users/register.html", {"form": UserCreationForm()})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(reverse("login"))

        return render(request, "users/register.html", {"form": form})


class LoginView(View):
    def get(self, request):
        return render(request, "users/login.html", {"form": AuthenticationForm})

    # really low level
    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data.get("username"),
                password=form.cleaned_data.get("password"),
            )

            if user is None:
                return render(
                    request, "users/login.html", {"form": form, "invalid_creds": True}
                )

            try:
                form.confirm_login_allowed(user)

            except ValidationError:
                return render(
                    request, "users/login.html", {"form": form, "invalid_creds": True}
                )
            login(request, user)

            return redirect(reverse("home"))
