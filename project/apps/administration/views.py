import math

# ============================================================================ #

from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms import inlineformset_factory
from django.contrib.admin.views.decorators import user_passes_test
from django.db.models import Avg
from django.contrib import messages
from django.contrib.auth import get_user_model

# ============================================================================ #
from project.apps.book.models import Category, Book, BookSlider, Tag, BookComment
from project.apps.common.models import HomeSlider
from project.apps.order.models import Order, Shipping
from project.apps.administration.forms import (
    CategoryForm,
    BookSliderForm,
    BookForm,
    TagForm,
    BookCommentForm,
    HomeSliderForm,
    ShippingForm,
    UserEditForm,
)

User = get_user_model()

# ========================== CREATE YOUR VIEWS HERE. ========================= #


# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: #
#                                   DECORATOR                                  #
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: #

# :::::::::::::::::::::::::::::: ADMIN REQUIRED :::::::::::::::::::::::::::::: #


def admin_required(view_func):
    decorated_view_func = user_passes_test(lambda u: u.is_superuser, login_url="login")(
        view_func
    )
    return decorated_view_func


# :::::::::::::::::::::::::::::: SELLER REQUIRED ::::::::::::::::::::::::::::: #


def seller_required(view_func):
    decorated_view_func = user_passes_test(
        lambda u: u.is_staff or u.is_superuser, login_url="login"
    )(view_func)
    return decorated_view_func


def index(request):

    return render(request, "administration/dashboard.html")


# ============================================================================ #
#                                 CATEGORY BOOK                                #
# ============================================================================ #


@seller_required
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


@admin_required
def category_create(request):

    form = CategoryForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        messages.success(request, "Malumotlaringiz saqlandi")
        return redirect("category_admin")

    context = {"form": form}

    return render(request, "administration/category/category_create.html", context)


# ============================================================================ #


@admin_required
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


@admin_required
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    messages.success(request, "Malumotlaringiz o'chirildi")
    return redirect("category_admin")


# ============================================================================ #
#                                     BOOK                                     #
# ============================================================================ #


@seller_required
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


@admin_required
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


@admin_required
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


@admin_required
def book_delete(request, pk):
    book = Book.objects.get(id=pk)
    book.delete()
    messages.success(request, "Malumotlaringiz o'chirildi")
    return redirect("book_admin")


# ============================================================================ #
#                                   TAG BOOK                                   #
# ============================================================================ #


@seller_required
def tag_book_admin(request):
    tags = Tag.objects.all()
    paginator = Paginator(tags, 10)
    page = request.GET.get("page")
    try:
        tags = paginator.page(page)
    except PageNotAnInteger:
        tags = paginator.page(1)
    except EmptyPage:
        tags = paginator.page(paginator.num_pages)
    context = {"tags": tags}
    return render(request, "administration/tag_book/tag_book_admin.html", context)


# ============================================================================ #


@admin_required
def tag_book_create(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Tag qoshildi")
            return redirect("tag_admin")
    else:
        form = TagForm()
    context = {"form": form}
    return render(request, "administration/tag_book/tag_book_create.html", context)


# ============================================================================ #


@admin_required
def tag_book_edit(request, pk):
    tag = Tag.objects.get(pk=pk)
    if request.method == "POST":
        form = TagForm(request.POST, request.FILES, instance=tag)
        if form.is_valid():
            form.save()
            messages.success(request, "Tag yangilandi")
            return redirect("tag_admin")
    else:
        form = TagForm(instance=tag)
    context = {"form": form, "tag": tag}
    return render(request, "administration/tag_book/tag_book_edit.html", context)


# ============================================================================ #


@admin_required
def tag_book_delete(request, pk):
    tag = Tag.objects.get(pk=pk)
    tag.delete()
    messages.success(request, "Tag o'chirildi")
    return redirect("tag_admin")


# ============================================================================ #


# ============================================================================ #
#                                 BOOK COMMENT                                 #
# ============================================================================ #


@seller_required
def book_comment_admin(request):
    book_comments = BookComment.objects.all()

    context = {"book_comments": book_comments}
    return render(
        request, "administration/book_comment/book_comment_admin.html", context
    )


# ============================================================================ #


@seller_required
def book_comment_detail(request, pk):
    book_comment = BookComment.objects.get(pk=pk)
    context = {"book_comment": book_comment}
    return render(
        request, "administration/book_comment/book_comment_detail.html", context
    )


# ============================================================================ #


@seller_required
def book_comment_edit(request, pk):
    book_comment = BookComment.objects.get(pk=pk)
    if request.method == "POST":
        form = BookCommentForm(request.POST, instance=book_comment)
        if form.is_valid():
            form.save()
            messages.success(request, "Savollar yangilandi")
            return redirect("book_comment_admin")
    else:
        form = BookCommentForm(instance=book_comment)
    context = {"form": form, "book_comment": book_comment}
    return render(
        request, "administration/book_comment/book_comment_edit.html", context
    )


# ============================================================================ #


@admin_required
def book_comment_delete(request, pk):
    book_comment = BookComment.objects.get(pk=pk)
    book = Book.objects.get(pk=book_comment.book.id)
    book_comment.delete()
    reviews = BookComment.objects.filter(book=book, status="True").aggregate(
        avarage=Avg("rate")
    )
    if reviews["avarage"] is None:
        book.rating = 0
        book.save()
    else:

        book.rating = math.ceil((reviews["avarage"]))
    book.save()
    messages.success(request, "Savollar o'chirildi")
    return redirect("book_comment_admin")


# ============================================================================ #
#                                  HOME SLIDER                                 #
# ============================================================================ #


@seller_required
def home_slider_admin(request):
    home_sliders = HomeSlider.objects.all()
    paginator = Paginator(home_sliders, 10)
    page = request.GET.get("page")
    try:
        home_sliders = paginator.page(page)
    except PageNotAnInteger:
        home_sliders = paginator.page(1)
    except EmptyPage:
        home_sliders = paginator.page(paginator.num_pages)
    context = {"home_sliders": home_sliders}
    return render(request, "administration/home_slider/home_slider_admin.html", context)


# ============================================================================ #


@admin_required
def home_slider_create(request):

    form = HomeSliderForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        messages.success(request, "Malumotlaringiz saqlandi")
        return redirect("home_slider_admin")

    context = {"form": form}

    return render(
        request, "administration/home_slider/home_slider_create.html", context
    )


# ============================================================================ #


@admin_required
def home_slider_edit(request, pk):
    home_slider = get_object_or_404(HomeSlider, pk=pk)
    form = HomeSliderForm(
        request.POST or None, request.FILES or None, instance=home_slider
    )

    if form.is_valid():
        form.save()
        messages.success(request, "Malumotlaringiz yangilandi")
        return redirect("home_slider_admin")

    context = {"form": form}

    return render(request, "administration/home_slider/home_slider_edit.html", context)


# ============================================================================ #


@admin_required
def home_slider_delete(request, pk):
    home_slider = get_object_or_404(HomeSlider, pk=pk)
    home_slider.delete()
    messages.success(request, "Malumotlaringiz o'chirildi")
    return redirect("home_slider_admin")


# ============================================================================ #
#                                     ORDER                                    #
# ============================================================================ #


@seller_required
def order_list(request):

    if request.method == "POST":
        order_id = request.POST["order_code"]
        customer = request.POST["name"]
        order_status = request.POST["status"]
        price_from = request.POST["price_from"]
        price_to = request.POST["price_to"]
        created_date = request.POST["created_date"]
        updated_date = request.POST["updated_date"]

        if order_id:
            orders = Order.objects.filter(id=order_id, is_paid=True)
        else:
            orders = Order.objects.filter(is_paid=True)

        if customer:
            orders = orders.filter(user__username__icontains=customer)
        if order_status:
            orders = orders.filter(status=order_status)
        if price_from:
            orders = orders.filter(total__gte=price_from)
        if price_to:
            orders = orders.filter(total__lte=price_to)
        if created_date:
            orders = orders.filter(create_at__icontains=created_date)
        if updated_date:
            orders = orders.filter(update_at__icontains=updated_date)

    else:
        orders = Order.objects.filter(is_paid=True)

    paginator = Paginator(orders, 10)
    page = request.GET.get("page")
    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        orders = paginator.page(1)
    except EmptyPage:
        orders = paginator.page(paginator.num_pages)

    context = {
        "orders": orders,
    }

    return render(request, "administration/order/order_list.html", context)


# ============================================================================ #


@seller_required
def order_detail(request, id):
    if request.method == "POST":
        status = request.POST["status"]
        url = request.META.get("HTTP_REFERER")
        order = Order.objects.get(pk=id)
        order.status = status
        order.save()
        return redirect(url)
    else:
        order = Order.objects.get(pk=id)
        print(order.shipping)
        context = {"order": order}
        return render(request, "administration/order/order_detail.html", context)


# ============================================================================ #
#                                   SHIPPING                                   #
# ============================================================================ #


@seller_required
def shipping_admin(request):
    shippings = Shipping.objects.all()

    context = {"shippings": shippings}
    return render(request, "administration/shipping/shipping_admin.html", context)


# ============================================================================ #


@seller_required
def shipping_create(request):
    if request.method == "POST":
        form = ShippingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Malumotlar qoshildi")
            return redirect("shipping_admin")
    else:
        form = ShippingForm()
    context = {"form": form}
    return render(request, "administration/shipping/shipping_create.html", context)


# ============================================================================ #


@seller_required
def shipping_edit(request, pk):
    shipping = Shipping.objects.get(pk=pk)
    if request.method == "POST":
        form = ShippingForm(request.POST, instance=shipping)
        if form.is_valid():
            form.save()
            messages.success(request, "Malumotlar yangilandi")
            return redirect("shipping_admin")
    else:
        form = ShippingForm(instance=shipping)
    context = {"form": form, "shipping": shipping}
    return render(request, "administration/shipping/shipping_edit.html", context)


# ============================================================================ #


@seller_required
def shipping_delete(request, pk):
    shipping = Shipping.objects.get(pk=pk)
    shipping.delete()
    messages.success(request, "Malumotlar o'chirildi")
    return redirect("shipping_admin")


# ============================================================================ #
#                                     USER                                     #
# ============================================================================ #


@seller_required
def user_admin(request):

    if request.method == "POST":
        keyword = request.POST["keyword"]
        users = User.objects.filter(
            username__icontains=keyword,
            first_name__icontains=keyword,
            last_name__icontains=keyword,
        )

    else:
        keyword = {}
        users = User.objects.all()

    paginator = Paginator(users, 10)
    page = request.GET.get("page")
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    context = {
        "users": users,
        "keyword": keyword,
    }
    return render(request, "administration/user/user_admin.html", context)


# ============================================================================ #


@admin_required
def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    context = {
        "user": user,
    }
    return render(request, "administration/user/user_detail.html", context)


# ============================================================================ #


@admin_required
def user_edit(request, pk):

    user = get_object_or_404(User, pk=pk)
    form = UserEditForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        messages.success(request, "Malumotlaringiz yangilandi")
        return redirect("user_admin")

    context = {"form": form}

    return render(request, "administration/user/user_edit.html", context)


# ============================================================================ #


@admin_required
def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    messages.success(request, "Malumotlaringiz o'chirildi")
    return redirect("user_admin")
