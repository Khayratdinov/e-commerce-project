from django.shortcuts import render


# ========================== CREATE YOUR VIEWS HERE. ========================= #


def index(request):

    return render(request, "administration/dashboard.html")
