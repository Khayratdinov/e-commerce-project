from django.shortcuts import render

# ============================================================================ #
from project.apps.book.models import Category, Tag, Book

# Create your views here.


def book_list(request):
    books = Book.objects.all()

    context = {"books": books}
    return render(request, "book/book_list.html", context)


def book_detail(request):
    pass
