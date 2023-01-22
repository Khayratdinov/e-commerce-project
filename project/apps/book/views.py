import math

# ============================================================================ #
from django.shortcuts import render, get_object_or_404
from django.db.models import Avg
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.utils.translation import gettext as _
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# ============================================================================ #
from project.apps.book.models import Category, Tag, Book, BookSlider, BookComment
from project.apps.book.forms import BookCommentForm
from project.apps.common.models import HeadImages
from project.apps.core.utils import paginate_queryset


# ============================================================================ #
#                                     BOOK                                     #
# ============================================================================ #


SORT_FIELDS = {
    "name_A_Z": "title",
    "name_Z_A": "-title",
    "price_low_to_high": "price",
    "price_high_to_low": "-price",
    "rating_highest": "-rating",
    "rating_lowest": "rating",
    "added_date_old_new": "-id",
    "added_date_new_old": "id",
}


def book_list(request):
    book_list = Book.objects.filter(status="True")

    if request.method == "POST":
        select = request.POST.get("sort")
        sort_field = SORT_FIELDS.get(select, None)
        if sort_field is not None:
            book_list = book_list.order_by(sort_field)

    book_list = paginate_queryset(request, book_list)
    bradcaump_img = HeadImages.objects.filter(status=True).order_by("?")[:1]

    context = {"book_list": book_list, "bradcaump_img": bradcaump_img}
    return render(request, "book/book_list.html", context)


def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)

    bradcaump_img = HeadImages.objects.filter(status=True).order_by("?")[:1]
    book_slider = BookSlider.objects.filter(book=book)

    comments = BookComment.objects.filter(book=book)

    category_list = Category.objects.filter(book=book)
    books_by_category = Book.objects.filter(category__in=category_list, status="True")
    tags = Tag.objects.filter(book=book)

    random_books = Book.objects.filter(status="True").order_by("?")[:4]

    context = {
        "book": book,
        "bradcaump_img": bradcaump_img,
        "book_slider": book_slider,
        "comments": comments,
        "category_list": category_list,
        "books_by_category": books_by_category,
        "tags": tags,
        "random_books": random_books,
    }

    return render(request, "book/book_detail.html", context)


def book_list_by_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    books = Book.objects.filter(category=category)
    bradcaump_img = HeadImages.objects.filter(status=True).order_by("?")[:1]

    books = paginate_queryset(request, books)

    context = {"category": category, "books": books, "bradcaump_img": bradcaump_img}
    return render(request, "book/book_list_by_category.html", context)


def book_list_by_tag(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    books = Book.objects.filter(tags=tag)
    bradcaump_img = HeadImages.objects.filter(status=True).order_by("?")[:1]

    books = paginate_queryset(request, books)

    context = {"tag": tag, "books": books, "bradcaump_img": bradcaump_img}
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
