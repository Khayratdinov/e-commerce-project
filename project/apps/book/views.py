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


def book_detail(request, pk):
    book = Book.objects.filter(pk=pk)
    book_slider = BookSlider.objects.filter(book=book)

    context = {"book": book, "book_slider": book_slider}

    return render(request, "book/book_detail.html", context)


def book_list_by_category(request, pk):
    category = Category.objects.filter(pk=pk)
    books = Book.objects.filter(category=category)

    context = {"category": category, "books": books}
    return render(request, "book/book_detail.html", context)


def book_list_by_tag(request, pk):
    tag = Tag.objects.filter(pk=pk)
    books = Book.objects.filter(tags=tag)

    context = {"tag": tag, "books": books}
    return render(request, "book/book_detail.html", context)
