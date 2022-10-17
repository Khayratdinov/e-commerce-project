from django.shortcuts import render

# ============================================================================ #
from project.apps.book.models import Category, Tag, Book, BookSlider


# ============================================================================ #
#                                     BOOK                                     #
# ============================================================================ #


def book_list(request):
    books = Book.objects.all()

    context = {"books": books}
    return render(request, "book/book_list.html", context)


def book_detail(request, slug):
    book = Book.objects.filter(slug=slug)
    book_slider = BookSlider.objects.filter(book=book)

    context = {"book": book, "book_slider": book_slider}

    return render(request, "book/book_detail.html", context)


def book_list_by_category(request, slug):
    category = Category.objects.filter(slug=slug)
    books = Book.objects.filter(category=category)

    context = {"category": category, "books": books}
    return render(request, "book/book_detail.html", context)


def book_list_by_tag(request, slug):
    tag = Tag.objects.filter(slug=slug)
    books = Book.objects.filter(tags=tag)

    context = {"tag": tag, "books": books}
    return render(request, "book/book_detail.html", context)
