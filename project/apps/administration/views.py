from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms import inlineformset_factory
from django.contrib import messages

# ============================================================================ #
from project.apps.book.models import Category, Book, BookSlider, Tag
from project.apps.administration.forms import CategoryForm, BookSliderForm, BookForm

# ========================== CREATE YOUR VIEWS HERE. ========================= #


def index(request):

    return render(request, "administration/dashboard.html")


# ============================================================================ #
#                                 CATEGORY BOOK                                #
# ============================================================================ #


def category_admin(request):
    categories = Category.objects.all()
    paginator = Paginator(categories, 10)
    page = request.GET.get("page")
    try:
        categories = paginator.page(page)
    except PageNotAnInteger:
        categories = paginator.page(1)
    except EmptyPage:
        categories = paginator.page(paginator.num_pages)
    context = {"categories": categories}
    return render(request, "administration/category/category_admin.html", context)


# ============================================================================ #


def category_create(request):

    form = CategoryForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        messages.success(request, "Malumotlaringiz saqlandi")
        return redirect("category_admin")

    context = {"form": form}

    return render(request, "administration/category/category_create.html", context)


# ============================================================================ #


def category_edit(request, pk):

    category = get_object_or_404(Category, pk=pk)
    form = CategoryForm(request.POST or None, request.FILES or None, instance=category)

    if form.is_valid():
        form.save()
        messages.success(request, "Malumotlaringiz yangilandi")
        return redirect("category_admin")

    context = {"form": form}

    return render(request, "administration/category/category_edit.html", context)


# ============================================================================ #


def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    messages.success(request, "Malumotlaringiz o'chirildi")
    return redirect("category_admin")


# ============================================================================ #
#                                     BOOK                                     #
# ============================================================================ #


def book_admin(request):

    if request.method == "POST":
        keyword = request.POST["keyword"]
        category_select = request.POST["category_select"]
        if category_select == "all":
            books = Book.objects.filter(title__icontains=keyword)
        else:
            books = Book.objects.filter(
                title__icontains=keyword, category__title=category_select
            )

    else:
        books = Book.objects.all()

    categories = Category.objects.values_list("title", flat=True).distinct()
    paginator = Paginator(books, 10)
    page = request.GET.get("page")
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)
    context = {"books": books, "categories": categories}
    return render(request, "administration/book/book_admin.html", context)


# ============================================================================ #


def book_create(request):
    book = Book()

    bookInlineFormset = inlineformset_factory(
        Book,
        BookSlider,
        form=BookSliderForm,
        fields=(
            "book",
            "image",
        ),
        extra=2,
        can_delete=False,
        min_num=1,
        validate_min=True,
    )

    if request.method == "POST":

        formset = bookInlineFormset(
            request.POST or None, request.FILES or None, instance=book, prefix="images"
        )

        form = BookForm(
            request.POST or None, request.FILES or None, instance=book, prefix="book"
        )

        if form.is_valid() and formset.is_valid():
            form = form.save(commit=False)

            book.save()
            tags_list = request.POST.getlist("book-tags")
            tags = Tag.objects.filter(id__in=tags_list)
            book.tags.set(tags)
            for category in request.POST.getlist("book-category"):
                book.category.add(category)
            formset.save()
            messages.success(request, "Malumotlaringiz saqlandi")
            return redirect("book_admin")
    else:
        formset = bookInlineFormset(instance=book, prefix="images")
        form = BookForm(instance=book, prefix="book")
    context = {"form": form, "formset": formset}
    return render(request, "administration/book/book_create.html", context)


# ============================================================================ #


def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)

    bookInlineFormset = inlineformset_factory(
        Book,
        BookSlider,
        form=BookSliderForm,
        fields=(
            "book",
            "image",
        ),
        extra=2,
        can_delete=True,
        min_num=1,
        validate_min=True,
    )
    if request.method == "POST":
        formset = bookInlineFormset(
            request.POST or None, request.FILES or None, instance=book, prefix="images"
        )

        form = BookForm(
            request.POST or None, request.FILES or None, instance=book, prefix="book"
        )

        book.category.clear()
        for category in request.POST.getlist("book-category"):
            book.category.add(category)

        tags_list = request.POST.getlist("book-tags")
        tags = Tag.objects.filter(id__in=tags_list)
        book.tags.set(tags)
        if form.is_valid() and formset.is_valid():
            form = form.save(commit=False)
            form.save()
            formset.save()
            messages.success(request, "Malumotlaringiz yangilandi")
            return redirect("book_admin")

        else:

            print("Forms: ", form.errors)
            print("Formset: ", formset.errors)
    else:
        formset = bookInlineFormset(instance=book, prefix="images")
        form = BookForm(instance=book, prefix="book")
    context = {
        "form": form,
        "formset": formset,
    }
    return render(request, "administration/book/book_edit.html", context)


# ============================================================================ #


def book_delete(request, pk):
    book = Book.objects.get(id=pk)
    book.delete()
    messages.success(request, "Malumotlaringiz o'chirildi")
    return redirect("book_admin")
