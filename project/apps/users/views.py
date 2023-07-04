from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import PermissionDenied
from django.forms import ValidationError
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import messages

from project.apps.common.models import HeadImages
from project.apps.order.models import Order, OrderLineItem
from project.apps.book.models import Book

from .forms import (
    CustomUserCreationForm,
    CustomAuthenticationForm,
    CustomUserUpdateForm,
)

from django.views import View


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            phone = form.cleaned_data.get("phone")
            user = form.save()
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect("home")
        else:
            for field in form:
                for error in field.errors:
                    messages.error(request, error)
            return render(request, "users/register.html", {"form": form})
    else:
        form = CustomUserCreationForm()
    return render(request, "users/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            return redirect("home")
    else:
        form = CustomAuthenticationForm()
    return render(request, "users/login.html", {"form": form})


# @login_required
# def update_profile(request):
#     if request.method == "POST":
#         form = CustomUserUpdateForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             return redirect("home")
#     else:
#         form = CustomUserUpdateForm(instance=request.user)
#     return render(request, "users/profile.html", {"form": form})


# ============================================================================ #


@login_required
def view_profile(request):
    user = request.user
    if request.method == "POST":
        form = CustomUserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("view_profile")
    else:
        form = CustomUserUpdateForm(instance=user)

    orders_user = Order.objects.filter(user=user)

    context = {
        "orders_user": orders_user,
        "form": form,
        "user": user,
    }
    return render(request, "users/profile.html", context)


@login_required
def order_detail_user(request, order):
    order_detail = OrderLineItem.objects.filter(order=order)

    context = {
        "order_detail": order_detail,
    }

    return render(request, "users/user-order-detail.html", context)


@login_required
def add_wishlist(request, id):
    book = Book.objects.get(pk=id)
    request.user.book.add(book)
    return redirect(request.META.get("HTTP_REFERER"))


@login_required
def remove_wishlist(request, id):
    book = Book.objects.get(pk=id)
    request.user.book.remove(book)
    return redirect(request.META.get("HTTP_REFERER"))


@login_required
def wishlist(request):
    user = request.user

    wishlist = Book.objects.filter(wishlist=user)
    print("HELOOOORORORO", wishlist)
    context = {"wishlist": wishlist}
    return render(request, "users/wishlist.html", context)


@login_required()
def mylogout(request):
    logout(request)
    return HttpResponseRedirect("/")