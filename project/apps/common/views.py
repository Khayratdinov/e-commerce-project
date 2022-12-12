from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Sum
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.translation import get_language

# ============================================================================ #
from project.apps.common.models import (
    HomeSlider,
    ContactMessage,
    CommonInfo,
    HeadImages,
    FAQ,
)
from project.apps.common.forms import ContactMessageForm
from project.apps.book.models import Book
from project.apps.order.models import OrderLineItem
from project.apps.blog.models import Blog


# Create your views here.


def index(request):
    books = Book.objects.all()
    home_sliders = HomeSlider.objects.all()[:3]

    best_seller_books = (
        OrderLineItem.objects.filter()
        .values("product")
        .annotate(total_sales=Sum("quantity"))
        .order_by("-total_sales")[:8]
    )

    blog_posts = Blog.objects.filter(status="True")[:3]

    faqs = FAQ.objects.all()[:5]

    context = {
        "home_sliders": home_sliders,
        "books": books,
        "best_seller_books": best_seller_books,
        "blog_posts": blog_posts,
        "faqs": faqs,
    }

    return render(request, "index.html", context)


def contact_message(request):
    url = request.META.get("HTTP_REFERER")
    setting = CommonInfo.objects.filter(status="True").first()
    if request.method == "POST":

        form = ContactMessageForm(request.POST)

        if form.is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data["name"]
            data.phone = form.cleaned_data["phone"]
            data.subject = form.cleaned_data["subject"]
            data.message = form.cleaned_data["message"]
            data.ip = request.META.get("REMOTE_ADDR")
            data.save()
            messages.success(request, _("Sizning xabaringiz yuborildi! Rahmat"))
            return HttpResponseRedirect(url)

        messages.error(request, _("Xatolik yuz berdi iltimos qayta urinip koring"))
        return HttpResponseRedirect(url)
    form = ContactMessageForm
    bradcaump_img = HeadImages.objects.filter(status=True).order_by("?")[:1]
    context = {
        "form": form,
        "setting": setting,
        "bradcaump_img": bradcaump_img,
    }
    return render(request, "common/contact.html", context)


def search(request):
    lang = str(get_language())
    if request.method == "POST":
        search_text = request.POST["search_text"]
        if lang == "ru":
            news_list = Book.objects.filter(title_ru__icontains=search_text)
        elif lang == "uz":
            news_list = Book.objects.filter(title_uz__icontains=search_text)
        elif lang == "en":
            news_list = Book.objects.filter(title_en__icontains=search_text)
        else:
            news_list = Book.objects.filter(title__icontains=search_text)

        paginator = Paginator(news_list, 2)
        page = request.GET.get("page")
        try:
            news_list = paginator.page(page)
        except PageNotAnInteger:
            news_list = paginator.page(1)
        except EmptyPage:
            news_list = paginator.page(paginator.num_pages)

        context = {
            "news_list": news_list,
            "keyword": search_text,
        }
        return render(request, "common/search.html", context)
    return redirect("home")
