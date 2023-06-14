from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import gettext as _
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Sum
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.translation import get_language
from project.apps.core.utils import paginate_queryset

# ============================================================================ #
from project.apps.common.models import (
    HomeSlider,
    ContactMessage,
    CommonInfo,
    HeadImages,
    FAQ,
    About,
    ShippingInfo,
    PaymentInfo,
    DiscountInfo,
)
from project.apps.common.forms import ContactMessageForm
from project.apps.book.models import Book, CollectionBook
from project.apps.order.models import OrderLineItem
from project.apps.blog.models import Blog


# Create your views here.


def index(request):
    # from django.contrib.sessions.models import Session

    # Session.objects.all().delete()
    # Get all books
    books = Book.objects.all()
    collection_book = CollectionBook.objects.filter(status="True")
    special_collection_book = CollectionBook.objects.filter(
        status="True", special_status="True"
    )[:3]

    # Get the first three HomeSlider objects
    home_sliders = HomeSlider.objects.all()[:3]

    # Get the top 8 books based on sales
    best_seller_items = (
        OrderLineItem.objects.filter(collection_order_status=False)
        .values("product")
        .annotate(total_sales=Sum("quantity"))
        .order_by("-total_sales")[:8]
    )

    # Convert the queryset to a list of Book objects
    best_seller_books = []
    for book in best_seller_items:
        try:
            best_seller_books.append(Book.objects.get(id=book["product"]))
        except Book.DoesNotExist:
            pass

    # Get the first three Blog objects with status 'True'
    blog_posts = Blog.objects.filter(status="True")[:3]

    # Get the first five FAQ objects
    faqs = FAQ.objects.all()[:5]

    # Store the data in a context dictionary
    context = {
        "home_sliders": home_sliders,
        "books": books,
        "best_seller_books": best_seller_books,
        "blog_posts": blog_posts,
        "faqs": faqs,
        "collection_book": collection_book,
        "special_collection_book": special_collection_book,
    }

    # Render the response with the context data
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

    context = {
        "form": form,
        "setting": setting,
    }
    return render(request, "common/contact.html", context)


def search(request):
    lang = str(get_language())
    if request.method == "POST":
        search_text = request.POST["search_text"]
        if lang == "ru":
            book_list = Book.objects.filter(title_ru__icontains=search_text)
        elif lang == "uz":
            book_list = Book.objects.filter(title_uz__icontains=search_text)
        elif lang == "en":
            book_list = Book.objects.filter(title_en__icontains=search_text)
        else:
            book_list = Book.objects.filter(title__icontains=search_text)

        book_list = paginate_queryset(request, book_list)

        context = {
            "books": book_list,
            "keyword": search_text,
        }
        return render(request, "common/search.html", context)
    return redirect("home")


def shipping_info(request):
    shipping_info = ShippingInfo.objects.filter(status="True")
    return render(
        request, "common/shipping_info.html", {"shipping_info": shipping_info}
    )


def payment_info(request):
    payment_info = PaymentInfo.objects.filter(status="True")
    return render(request, "common/payment_info.html", {"payment_info": payment_info})


def discount_info(request):
    discount_info = DiscountInfo.objects.filter(status="True")
    return render(
        request, "common/discount_info.html", {"discount_info": discount_info}
    )


def about_info(request):
    about_info = About.objects.filter(status="True")
    return render(request, "common/about_info.html", {"about_info": about_info})