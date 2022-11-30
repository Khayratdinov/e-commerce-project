import math

# ============================================================================ #
from django.shortcuts import render, get_object_or_404
from django.db.models import Avg
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.utils.translation import gettext as _

# ============================================================================ #
from project.apps.book.models import Category, Tag, Book, BookSlider, BookComment
from project.apps.book.forms import BookCommentForm


# ============================================================================ #
#                                     BOOK                                     #
# ============================================================================ #


def book_list(request):
    book_list = Book.objects.all()

    context = {"book_list": book_list}
    return render(request, "book/book_list.html", context)


def book_detail(request, slug):
    book = Book.objects.get(slug=slug)
    book_slider = BookSlider.objects.filter(book=book)

    context = {"book": book, "book_slider": book_slider}

    return render(request, "book/book_detail.html", context)


def book_list_by_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    books = Book.objects.filter(category=category)

    context = {"category": category, "books": books}
    return render(request, "book/book_list_by_category.html", context)


def book_list_by_tag(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    books = Book.objects.filter(tags=tag)

    context = {"tag": tag, "books": books}
    return render(request, "book/book_list_by_tag.html", context)


def add_comment(request, book_id):
    url = request.META.get("HTTP_REFERER")
    book = Book.objects.filter(id=book_id)
    reviews = BookComment.objects.filter(book=book, status="True").aggregate(
        avarage=Avg("rate")
    )

    if request.method == "POST":
        form = BookCommentForm(request.POST)
        if form.is_valid():
            data = BookComment()
            data.book_id = book_id
            current_user = request.user
            data.user_id = current_user.id
            data.comment = form.cleaned_data["comment"]
            data.rate = form.cleaned_data["rate"]
            data.ip = request.META.get("REMOTE_ADDR")
            data.save()
            if reviews["avarage"] == None:
                book.rating = data.rate
            else:
                book.rating = math.ceil((reviews["avarage"]))
            book.save()
            messages.success(request, "Izohingiz qabul qilindi !")
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)
