import math
import datetime
import random

# ============================================================================ #
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms import inlineformset_factory
from django.contrib.admin.views.decorators import user_passes_test
from django.db.models import Avg, Sum
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.db import transaction


# ============================================================================ #
from project.apps.book.models import (
    Category,
    Book,
    BookSlider,
    Tag,
    BookComment,
    CollectionBook,
    CollectionSlider,
)
from project.apps.common.models import (
    HomeSlider,
    HeadImages,
    CommonInfo,
    ContactMessage,
    FAQ,
    About,
    ShippingInfo,
    PaymentInfo,
    DiscountInfo,
)
from project.apps.order.models import Order, Shipping, OrderLineItem
from project.apps.blog.models import CategoryBlog, Blog
from project.apps.administration.models import ShopCart
from project.apps.administration.forms import (
    CategoryForm,
    BookSliderForm,
    BookForm,
    TagForm,
    BookCommentForm,
    HomeSliderForm,
    ShippingForm,
    UserEditForm,
    ShopCartForm,
    BlogForm,
    CategoryBlogForm,
    RandomBradcaumpImgForm,
    CommonInfoForm,
    CollectionBookForm,
    CollectionSliderForm,
    FaqForm,
    AboutForm,
    ShippingInfoForm,
    PaymentInfoForm,
    DiscountInfoForm,
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


# ============================================================================ #
#                                   PAGINATOR                                  #
# ============================================================================ #


def paginate_queryset_admin(
    request, queryset, per_page=12, page_kwarg="page", order_by="-created_at"
):
    ordered_queryset = queryset.order_by(order_by)
    paginator = Paginator(ordered_queryset, per_page)
    page = request.GET.get(page_kwarg)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return page_obj


# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: #
#                                ADMIN DASHBOARD                               #
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: #


@seller_required
def index(request):
    new_orders = Order.objects.filter(is_paid=True, status="New").order_by(
        "-created_at"
    )
    new_orders_count = new_orders.count()

    new_messages = ContactMessage.objects.filter(status="False").order_by("-created_at")
    new_messages_count = new_messages.count()

    today_comments = BookComment.objects.filter(
        created_at=datetime.date.today()
    ).count()

    today_orders = Order.objects.filter(is_paid=True, created_at=datetime.date.today())
    today_orders_count = today_orders.count()

    total_sum = 0
    for order in today_orders:
        total_sum += order.total

    today_offline_orders = Order.objects.filter(
        created_at=datetime.date.today(), offline_sales=True
    )
    today_offline_orders_count = today_offline_orders.count()

    total_sum_offline = 0
    for order in today_offline_orders:
        total_sum_offline += order.total

    today_online_orders = Order.objects.filter(
        is_paid=True, created_at=datetime.date.today(), offline_sales=False
    )
    today_online_orders_count = today_online_orders.count()

    total_sum_online = 0
    for order in today_online_orders:
        total_sum_online += order.total

    context = {
        "new_orders_count": new_orders_count,
        "new_messages": new_messages,
        "new_orders": new_orders,
        "new_messages_count": new_messages_count,
        "today_comments": today_comments,
        "today_orders_count": today_orders_count,
        "total_sum": total_sum,
        "today_offline_orders_count": today_offline_orders_count,
        "total_sum_offline": total_sum_offline,
        "today_online_orders_count": today_online_orders_count,
        "total_sum_online": total_sum_online,
    }
    return render(request, "administration/dashboard.html", context)


# ============================================================================ #
#                               GENERAL DASHBOARD                              #
# ============================================================================ #


@seller_required
def general_dashboard(request):
    all_orders_count = Order.objects.filter(is_paid=True).count()

    total_sum_all_orders = (
        Order.objects.filter(is_paid=True).aggregate(Sum("total")).get("total__sum")
    )

    all_users_count = User.objects.all().count()

    all_staff_count = User.objects.filter(is_staff=True).count()

    all_books_count = Book.objects.all().count()

    all_offline_sales_count = Order.objects.filter(offline_sales=True).count()

    total_sum_all_offline_sales = (
        Order.objects.filter(offline_sales=True)
        .aggregate(Sum("total"))
        .get("total__sum")
    )

    all_online_sales_count = Order.objects.filter(
        is_paid=True, offline_sales=False
    ).count()

    total_sum_all_online_sales = (
        Order.objects.filter(is_paid=True, offline_sales=False)
        .aggregate(Sum("total"))
        .get("total__sum")
    )

    all_news_count = Blog.objects.all().count()

    all_book_comments_count = BookComment.objects.all().count()

    all_contact_message_count = ContactMessage.objects.all().count()

    context = {
        "all_orders_count": all_orders_count,
        "all_offline_sales_count": all_offline_sales_count,
        "total_sum_all_offline_sales": total_sum_all_offline_sales,
        "all_online_sales_count": all_online_sales_count,
        "total_sum_all_online_sales": total_sum_all_online_sales,
        "total_sum_all_orders": total_sum_all_orders,
        "all_users_count": all_users_count,
        "all_staff_count": all_staff_count,
        "all_books_count": all_books_count,
        "all_contact_message_count": all_contact_message_count,
        "all_book_comments_count": all_book_comments_count,
        "all_news_count": all_news_count,
    }
    return render(request, "administration/dashboard/general_dashboard.html", context)


# ============================================================================ #
#                               WEEKLY_DASHBOARD                               #
# ============================================================================ #


@seller_required
def weekly_dashboard(request):
    users_week = User.objects.filter(
        date_joined__week=datetime.date.today().isocalendar()[1]
    ).count()

    users_count = User.objects.all().count()

    # ========================= OTKAN HAFTANING MIJOZLARI ======================== #

    last_week_users = User.objects.filter(
        date_joined__week=datetime.date.today().isocalendar()[1] - 1
    ).count()

    # ========================== MIJOZLARNING OSISH % TA ========================= #

    if last_week_users == 0:
        last_week_and_this_week_count_users = 0
    else:
        last_week_and_this_week_count_users = (users_week / last_week_users - 1) * 100

    # ========================== UMIMIY BUYIRTMALAR SONI ========================= #

    orders_week = Order.objects.filter(
        is_paid=True, created_at__week=datetime.date.today().isocalendar()[1]
    )
    count_orders_week = orders_week.count()

    # ====================== UMIMIY BUYIRTMALARNING DAROMATI ===================== #
    total_price_week = 0
    for order in orders_week:
        total_price_week += order.total

    # ========================= OTKAN HAFTA BUYIRTMALARI ========================= #

    last_week_orders = Order.objects.filter(
        is_paid=True, created_at__week=datetime.date.today().isocalendar()[1] - 1
    )
    last_week_orders_count = last_week_orders.count()

    # ========================= OTKAN HAFTANING DAROMATI ========================= #

    last_week_total_price = 0

    for order in last_week_orders:
        last_week_total_price += order.total

    # ========================== BUYIRTMALAR OSISH % TA ========================== #

    if last_week_orders_count == 0:
        last_week_and_this_week_orders_count = 0
    else:
        last_week_and_this_week_orders_count = (
            count_orders_week / last_week_orders_count - 1
        ) * 100

    # ========================== DAROMATNING OSISH % TA ========================== #

    if last_week_total_price == 0:
        last_week_and_this_week_total_price = 0
    else:
        last_week_and_this_week_total_price = (
            total_price_week / last_week_total_price - 1
        ) * 100

    # ========================= OFFLINE BUYIRTMALAR SONI ========================= #

    offline_orders_week = Order.objects.filter(
        created_at__week=datetime.date.today().isocalendar()[1], offline_sales=True
    )
    offline_count_orders_week = offline_orders_week.count()

    # ======================= OFFLINE BUYIRTMALAR DAROMATI ======================= #

    offline_total_price_week = 0
    for order in offline_orders_week:
        offline_total_price_week += order.total

    # ========================== ONLINE BUYIRTMALAR SONI ========================= #

    online_orders_week = Order.objects.filter(
        created_at__week=datetime.date.today().isocalendar()[1],
        offline_sales=False,
        is_paid=True,
    )
    online_count_orders_week = online_orders_week.count()

    # ======================== ONLINE BUYIRTMALAR DAROMATI ======================= #

    online_total_price_week = 0
    for order in online_orders_week:
        online_total_price_week += order.total

    # =============== SHU HAFTANING ENG KOP SOTILGAN TOP 10 KITOBI =============== #

    best_seller_books = (
        OrderLineItem.objects.filter(
            collection_order_status=False,
            order__created_at__week=datetime.date.today().isocalendar()[1],
        )
        .values("product")
        .annotate(total=Sum("quantity"))
        .order_by("-total")[:10]
    )

    best_seller_books_list = []
    for book in best_seller_books:
        best_seller_books_list.append(Book.objects.get(id=book["product"]))

    # ============================= WEEKLY STATISTICS ============================ #

    # ================= SOTILGAN KITOBLAR SONI BOYICHA STATISTICA ================ #

    count_orders_day_in_week = []
    date = datetime.date.today()
    week = date - datetime.timedelta(date.weekday())
    weekdays = [week + datetime.timedelta(i) for i in range(7)]
    for day in weekdays:
        count_orders_day_in_week.append(
            Order.objects.filter(
                is_paid=True,
                created_at__day=day.day,
                created_at__month=day.month,
                created_at__year=day.year,
            ).count()
        )

    # ======================== DAROMAT BOYICHA STATISTICA ======================== #

    orders_day_in_week = []
    date = datetime.date.today()
    week = date - datetime.timedelta(date.weekday())
    weekdays = [week + datetime.timedelta(i) for i in range(7)]
    for day in weekdays:
        orders_day = Order.objects.filter(
            is_paid=True,
            created_at__day=day.day,
            created_at__month=day.month,
            created_at__year=day.year,
        )
        total_price_day = 0
        for order in orders_day:
            total_price_day += order.total
        orders_day_in_week.append(total_price_day)

    context = {
        "users_week": users_week,
        "users_count": users_count,
        "total_price_week": total_price_week,
        "count_orders_week": count_orders_week,
        "last_week_total_price": last_week_total_price,
        "last_week_and_this_week_total_price": last_week_and_this_week_total_price,
        "last_week_and_this_week_count_users": last_week_and_this_week_count_users,
        "last_week_users": last_week_users,
        "last_week_orders_count": last_week_orders_count,
        "last_week_and_this_week_orders_count": last_week_and_this_week_orders_count,
        "offline_total_price_week": offline_total_price_week,
        "offline_count_orders_week": offline_count_orders_week,
        "online_total_price_week": online_total_price_week,
        "online_count_orders_week": online_count_orders_week,
        "orders_week": orders_week,
        "best_seller_books_list": best_seller_books_list,
        "count_orders_day_in_week": count_orders_day_in_week,
        "orders_day_in_week": orders_day_in_week,
    }

    return render(request, "administration/dashboard/weekly_dashboard.html", context)


# ============================================================================ #


# ============================================================================ #
#                               MONTHLY DASHBOARD                              #
# ============================================================================ #


@seller_required
def monthly_dashboard(request):
    # ======================== SHU OYNING YANGI MIJOZLARI ======================== #

    users_month = User.objects.filter(
        date_joined__month=datetime.date.today().month
    ).count()
    users_count = User.objects.all().count()

    # ========================== OTKAN OYNING MIJOZLARI ========================== #

    last_month_users = User.objects.filter(
        date_joined__month=datetime.date.today().month - 1
    ).count()

    # =========================== MIJOZLAR OSISHI % TA =========================== #

    if last_month_users == 0:
        users_growth = 0
    else:
        users_growth = (users_month / last_month_users - 1) * 100

    # ======================== SHU OYNING BUYURTMALAR SONI ======================= #

    orders_month = Order.objects.filter(
        is_paid=True, created_at__month=datetime.date.today().month
    )
    count_orders_month = orders_month.count()

    # ======================= OTKAN OYNING BUYIRTMALAR SONI ====================== #

    last_month_orders = Order.objects.filter(
        is_paid=True, created_at__month=datetime.date.today().month - 1
    )
    last_month_orders_count = last_month_orders.count()

    # ========================== BUYIRTMALAR OSISHI % TA ========================= #

    if last_month_orders_count == 0:
        orders_growth = 0
    else:
        orders_growth = (count_orders_month / last_month_orders_count - 1) * 100

    # ============================ SHU OYNING DAROMATI =========================== #

    total_price_month = 0
    for order in orders_month:
        total_price_month += order.total

    # =========================== OTKAN OYNING DAROMATI ========================== #

    last_month_total_price = 0
    for order in last_month_orders:
        last_month_total_price += order.total

    # ============================ DAROMAT OSISHI % TA =========================== #

    if last_month_total_price == 0:
        total_price_growth = 0
    else:
        total_price_growth = (total_price_month / last_month_total_price - 1) * 100

    # =================== OFFLINE BUYURTMALAR SONI VA DAROMATI =================== #

    offline_orders_month = Order.objects.filter(
        created_at__month=datetime.date.today().month, offline_sales=True
    )
    offline_count_orders_month = offline_orders_month.count()
    offline_total_price_month = 0
    for order in offline_orders_month:
        offline_total_price_month += order.total

    # ==================== ONLINE BUYURTMALAR SONI VA DAROMATI =================== #

    online_orders_month = Order.objects.filter(
        is_paid=True, created_at__month=datetime.date.today().month, offline_sales=False
    )
    online_count_orders_month = online_orders_month.count()
    online_total_price_month = 0
    for order in online_orders_month:
        online_total_price_month += order.total

    # ========================= KOP SOTILGAN TOP 10 KITOB ======================== #

    best_seller_books = (
        OrderLineItem.objects.filter(
            collection_order_status=False,
            order__created_at__month=datetime.date.today().month,
        )
        .values("product")
        .annotate(total=Sum("quantity"))
        .order_by("-total")[:10]
    )

    best_seller_books_list = []
    for book in best_seller_books:
        best_seller_books_list.append(Book.objects.get(id=book["product"]))

    # ============================ MONTHLY STATISTICS ============================ #

    # ===================== SOTILGAN KITOBLAR SONI BOYICHA STATISTICA ============= #

    count_orders_day_in_month = []
    date = datetime.date.today()
    month = date - datetime.timedelta(date.day - 1)
    for i in range(0, date.day):
        count_orders_day_in_month.append(
            Order.objects.filter(
                is_paid=True,
                created_at__month=month.month,
                created_at__day=month.day + i,
            ).count()
        )

    # ======================== DAROMAT BOYICHA STATISTICA ======================== #

    total_price_day_in_month = []

    start_day = datetime.date.today().replace(day=1).day

    today = datetime.date.today().day
    for day in range(start_day, today + 1):
        orders_day = Order.objects.filter(
            is_paid=True,
            created_at__month=datetime.date.today().month,
            created_at__day=day,
        )
        total_price_day = 0
        for order in orders_day:
            total_price_day += order.total
        total_price_day_in_month.append(total_price_day)

    context = {
        "total_price_month": total_price_month,
        "count_orders_month": count_orders_month,
        "offline_count_orders_month": offline_count_orders_month,
        "offline_total_price_month": offline_total_price_month,
        "last_month_orders_count": last_month_orders_count,
        "orders_growth": orders_growth,
        "last_month_total_price": last_month_total_price,
        "total_price_growth": total_price_growth,
        "last_month_users": last_month_users,
        "users_growth": users_growth,
        "online_count_orders_month": online_count_orders_month,
        "online_total_price_month": online_total_price_month,
        "best_seller_books_list": best_seller_books_list,
        "users_month": users_month,
        "users_count": users_count,
        "count_orders_day_in_month": count_orders_day_in_month,
        "total_price_day_in_month": total_price_day_in_month,
    }

    return render(request, "administration/dashboard/monthly_dashboard.html", context)


# ============================================================================ #
#                               YEARLY DASHBOARD                               #
# ============================================================================ #


@seller_required
def yearly_dashboard(request):
    # =========================== SHU YILNING MIJOZLARI ========================== #

    users_year = User.objects.filter(
        date_joined__year=datetime.date.today().year
    ).count()
    users_count = User.objects.all().count()

    # ======================= BUYURTMALAR SONI VA DAROMATI ======================= #

    orders_year = Order.objects.filter(
        is_paid=True, created_at__year=datetime.date.today().year
    )
    count_orders_year = orders_year.count()

    total_price_year = 0
    for order in orders_year:
        total_price_year += order.total

    # =================== OFFLINE BUYURTMALAR SONI VA DAROMATI =================== #

    offline_orders_year = Order.objects.filter(
        created_at__year=datetime.date.today().year, offline_sales=True
    )
    offline_count_orders_year = offline_orders_year.count()
    offline_total_price_year = 0
    for order in offline_orders_year:
        offline_total_price_year += order.total

    # ==================== ONLINE BUYURTMALAR SONI VA DAROMATI =================== #

    online_orders_year = Order.objects.filter(
        is_paid=True, created_at__year=datetime.date.today().year, offline_sales=False
    )
    online_count_orders_year = online_orders_year.count()
    online_total_price_year = 0
    for order in online_orders_year:
        online_total_price_year += order.total

    # ========================= KOP SOTILGAN TOP 10 KITOB ======================== #

    best_seller_books = (
        OrderLineItem.objects.filter(
            collection_order_status=False,
            order__created_at__year=datetime.date.today().year,
        )
        .values("product")
        .annotate(total=Sum("quantity"))
        .order_by("-total")[:10]
    )

    best_seller_books_list = []
    for book in best_seller_books:
        best_seller_books_list.append(Book.objects.get(id=book["product"]))

    # ============================= YEARLY STATISTICS ============================ #

    # ===================== SOTILGAN KITOBLAR SONI BOYICHA STATISTICA ============= #

    count_orders_month_in_year = []
    start_month = datetime.date.today().replace(month=1).month
    today_month = datetime.date.today().month
    for month in range(start_month, today_month + 1):
        count_orders_month_in_year.append(
            Order.objects.filter(
                is_paid=True,
                created_at__month=month,
                created_at__year=datetime.date.today().year,
            ).count()
        )

    # ======================== DAROMAT BOYICHA STATISTICA ======================== #

    total_price_month_in_year = []
    start_month = datetime.date.today().replace(month=1).month
    today_month = datetime.date.today().month
    for month in range(start_month, today_month + 1):
        orders_month = Order.objects.filter(
            is_paid=True,
            created_at__year=datetime.date.today().year,
            created_at__month=month,
        )
        total_price_month = 0
        for order in orders_month:
            total_price_month += order.total
        total_price_month_in_year.append(total_price_month)

    context = {
        "total_price_year": total_price_year,
        "count_orders_year": count_orders_year,
        "offline_count_orders_year": offline_count_orders_year,
        "offline_total_price_year": offline_total_price_year,
        "online_count_orders_year": online_count_orders_year,
        "online_total_price_year": online_total_price_year,
        "best_seller_books_list": best_seller_books_list,
        "users_year": users_year,
        "users_count": users_count,
        "orders_year": orders_year,
        "count_orders_month_in_year": count_orders_month_in_year,
        "total_price_month_in_year": total_price_month_in_year,
    }
    return render(request, "administration/dashboard/yearly_dashboard.html", context)


# ============================================================================ #
#                                 CATEGORY BOOK                                #
# ============================================================================ #


@seller_required
def category_admin(request):
    categories = Category.objects.all()
    categories = paginate_queryset_admin(request, categories)
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
    keyword = request.POST.get("keyword", "")
    category_select = request.POST.get("category_select", "all")

    books = Book.objects.all()

    if keyword:
        books = books.filter(title__icontains=keyword)
        if category_select != "all":
            books = books.filter(category__title=category_select)

    categories = Category.objects.values_list("title", flat=True).distinct()
    books = paginate_queryset_admin(request, books)
    context = {
        "books": books,
        "categories": categories,
        "keyword": keyword,
        "category_select": category_select,
    }
    return render(request, "administration/book/book_admin.html", context)


# ============================================================================ #


@admin_required
def book_create(request):
    book = Book()

    BookInlineFormset = inlineformset_factory(
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
        formset = BookInlineFormset(
            request.POST or None, request.FILES or None, instance=book, prefix="images"
        )
        form = BookForm(
            request.POST or None, request.FILES or None, instance=book, prefix="book"
        )
        form.fields["coverpage"].widget.attrs["required"] = True

        if form.is_valid() and formset.is_valid():
            with transaction.atomic():
                book = form.save(commit=False)
                book.save()
                form.save_m2m()

                formset.instance = book
                formset.save()

            messages.success(request, "Malumotlaringiz saqlandi")
            return redirect("book_admin")
    else:
        formset = BookInlineFormset(instance=book, prefix="images")
        form = BookForm(instance=book, prefix="book")
    context = {"form": form, "formset": formset}
    return render(request, "administration/book/book_create.html", context)


# ============================================================================ #


BookSliderFormset = inlineformset_factory(
    Book,
    BookSlider,
    fields=("book", "image"),
    extra=2,
    can_delete=True,
    min_num=1,
    validate_min=True,
)


@admin_required
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book_form_prefix = "book"
    images_form_prefix = "images"

    if request.method == "POST":
        form = BookForm(
            request.POST or None,
            request.FILES or None,
            instance=book,
            prefix=book_form_prefix,
        )
        formset = BookSliderFormset(
            request.POST or None,
            request.FILES or None,
            instance=book,
            prefix=images_form_prefix,
            queryset=BookSlider.objects.filter(book=book),
        )

        if form.is_valid() and formset.is_valid():
            with transaction.atomic():
                form = form.save(commit=False)
                form.save()
                formset.save()

                book.category.set(request.POST.getlist("book-category"))
                book.tags.set(
                    Tag.objects.filter(id__in=request.POST.getlist("book-tags"))
                )
                book.collection_book.set(
                    CollectionBook.objects.filter(
                        id__in=request.POST.getlist("book-collection_book")
                    )
                )

                messages.success(request, "Malumotlaringiz yangilandi")
                return redirect("book_admin")
    else:
        form = BookForm(instance=book, prefix=book_form_prefix)
        formset = BookSliderFormset(
            instance=book,
            prefix=images_form_prefix,
            queryset=BookSlider.objects.filter(book=book),
        )

    form.fields["coverpage"].widget.attrs["required"] = False

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
    tags = paginate_queryset_admin(request, tags)
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
    book_comment = get_object_or_404(BookComment, pk=pk)
    book = book_comment.book
    book_comment.delete()

    reviews = BookComment.objects.filter(book=book, status="True").aggregate(
        avarage=Avg("rate")
    )

    book.rating = 0 if reviews["avarage"] is None else math.ceil((reviews["avarage"]))
    book.count_comment -= 1
    book.save()
    messages.success(request, "Savollar o'chirildi")
    return redirect("book_comment_admin")


# ============================================================================ #
#                                  HOME SLIDER                                 #
# ============================================================================ #


@seller_required
def home_slider_admin(request):
    home_sliders = HomeSlider.objects.all()
    home_sliders = paginate_queryset_admin(request, home_sliders)
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
    # orders order by created date
    orders = Order.objects.filter(is_paid=True)

    if request.method == "POST":
        order_id = request.POST.get("order_code")
        customer = request.POST.get("name")
        order_status = request.POST.get("status")
        price_from = request.POST.get("price_from")
        price_to = request.POST.get("price_to")
        created_date = request.POST.get("created_date")
        updated_date = request.POST.get("updated_date")

        if order_id:
            orders = orders.filter(order_code=order_id)

        if customer:
            orders = orders.filter(full_name__icontains=customer)

        if order_status:
            orders = orders.filter(status=order_status)

        if price_from:
            orders = orders.filter(total__gte=price_from)

        if price_to:
            orders = orders.filter(total__lte=price_to)

        if created_date:
            orders = orders.filter(created_at__icontains=created_date)

        if updated_date:
            orders = orders.filter(updated_at__icontains=updated_date)

    order_list = paginate_queryset_admin(request, orders)

    context = {
        "orders": order_list,
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
        ).order_by("-date_joined")

    else:
        keyword = {}
        users = User.objects.all().order_by("-date_joined")

    users = paginate_queryset_admin(request, users, order_by="-date_joined")
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


# ============================================================================ #
#                                   SHOP CART                                  #
# ============================================================================ #


@seller_required
def add_to_shopcart(request, slug):
    url = request.META.get("HTTP_REFERER")
    current_user = request.user
    product = Book.objects.get(slug=slug)
    if request.method == "POST":
        form = ShopCartForm(request.POST)
        if form.is_valid():
            data = ShopCart()
            data.user_id = current_user.id
            data.product_id = product.id
            data.quantity = form.cleaned_data["quantity"]

            data.save()
        messages.success(request, "Mahsulot qoshildi")
        return HttpResponseRedirect(url)

    else:
        data = ShopCart()
        data.user_id = current_user.id
        data.product_id = id
        data.quantity = 1
        data.save()  #
        messages.success(request, "Mahsulot qoshildi")
        return HttpResponseRedirect(url)


@seller_required
def shopcart(request):
    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    total = 0
    for rs in shopcart:
        total += rs.product.price * rs.quantity
    context = {
        "shopcart": shopcart,
        "total": total,
    }
    return render(request, "administration/order/shopCart_admin.html", context)


def order_create_admin(request):
    admin = request.user
    shopcart_admin = ShopCart.objects.all()
    total_price = 0
    for shopcart in shopcart_admin:
        total_price += shopcart.product.price * shopcart.quantity
    code = random.randint(10000000, 99999999)
    order = Order.objects.create(
        user=admin,
        order_code=code,
        full_name="Hamrohbooks admin",
        total=total_price,
        offline_sales=True,
        is_paid=True,
    )
    order.save()

    for shopcart in shopcart_admin:
        orderproduct = OrderLineItem.objects.create(
            order=order,
            product=shopcart.product,
            quantity=shopcart.quantity,
        )
        orderproduct.save()
        shopcart.delete()
    messages.success(request, "Buyirtma muaffaqiyatli qoshildi")
    return redirect("dashboard")


@seller_required
def delete_from_cart(request, id):
    url = request.META.get("HTTP_REFERER")
    ShopCart.objects.filter(id=id).delete()
    messages.success(request, "Mahsulot o'chirildi")
    return HttpResponseRedirect(url)


# ============================================================================ #
#                                  ORDER ADMIN                                 #
# ============================================================================ #


@seller_required
def order_dashboard(request):
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
    books = paginate_queryset_admin(request, books)
    context = {"books": books, "categories": categories}
    return render(request, "administration/order/order_dashboard.html", context)


# ============================================================================ #
#                                 BLOG CATEGORY                                #
# ============================================================================ #


@seller_required
def category_blog_admin(request):
    categories = CategoryBlog.objects.all()
    categories = paginate_queryset_admin(request, categories)
    context = {"categories": categories}
    return render(
        request, "administration/category_blog/category_blog_admin.html", context
    )


# ============================================================================ #


@seller_required
def category_blog_create(request):
    if request.method == "POST":
        form = CategoryBlogForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Categori qoshildi")
            return redirect("category_blog_admin")
    else:
        form = CategoryBlogForm()
    context = {"form": form}
    return render(
        request, "administration/category_blog/category_blog_create.html", context
    )


# ============================================================================ #


@seller_required
def category_blog_edit(request, pk):
    category = CategoryBlog.objects.get(pk=pk)
    if request.method == "POST":
        form = CategoryBlogForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, "Categori yangilandi")
            return redirect("category_blog_admin")
    else:
        form = CategoryBlogForm(instance=category)
    context = {"form": form, "category": category}
    return render(
        request, "administration/category_blog/category_blog_edit.html", context
    )


# ============================================================================ #


@seller_required
def category_blog_delete(request, pk):
    category = CategoryBlog.objects.get(pk=pk)
    category.delete()
    messages.success(request, "Categori o'chirildi")
    return redirect("category_blog_admin")


# ============================================================================ #


# ============================================================================ #
#                                     BLOG                                     #
# ============================================================================ #


@seller_required
def blog_admin(request):
    blogs = Blog.objects.all()
    blogs = paginate_queryset_admin(request, blogs)
    context = {"blogs": blogs}
    return render(request, "administration/blog/blog_admin.html", context)


# ============================================================================ #


@seller_required
def blog_create(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Blog qoshildi")
            return redirect("blog_admin")
    else:
        form = BlogForm()
    context = {"form": form}
    return render(request, "administration/blog/blog_create.html", context)


# ============================================================================ #


@seller_required
def blog_edit(request, pk):
    blog = Blog.objects.get(pk=pk)
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, "Blog yangilandi")
            return redirect("blog_admin")
    else:
        form = BlogForm(instance=blog)
    context = {"form": form, "blog": blog}
    return render(request, "administration/blog/blog_edit.html", context)


# ============================================================================ #


@seller_required
def blog_delete(request, pk):
    blog = Blog.objects.get(pk=pk)
    blog.delete()
    messages.success(request, "Blog o'chirildi")
    return redirect("blog_admin")


# ============================================================================ #


# ============================================================================ #
#                            RANDOM BRADCAUMP IMAGES                           #
# ============================================================================ #


@seller_required
def random_image_admin(request):
    images = HeadImages.objects.all()
    images = paginate_queryset_admin(request, images)
    context = {"images": images}
    return render(
        request, "administration/random_image/random_image_admin.html", context
    )


# ============================================================================ #


@seller_required
def random_image_create(request):
    if request.method == "POST":
        form = RandomBradcaumpImgForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Rasmlar qoshildi")
            return redirect("random_image_admin")
    else:
        form = RandomBradcaumpImgForm()
    context = {"form": form}
    return render(
        request, "administration/random_image/random_image_create.html", context
    )


# ============================================================================ #


@seller_required
def random_image_edit(request, pk):
    image = HeadImages.objects.get(pk=pk)
    if request.method == "POST":
        form = RandomBradcaumpImgForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            messages.success(request, "Rasmlar yangilandi")
            return redirect("random_image_admin")
    else:
        form = RandomBradcaumpImgForm(instance=image)
    context = {"form": form, "image": image}
    return render(
        request, "administration/random_image/random_image_edit.html", context
    )


# ============================================================================ #


@seller_required
def random_image_delete(request, pk):
    image = HeadImages.objects.get(pk=pk)
    image.delete()
    messages.success(request, "Rasmlar o'chirildi")
    return redirect("random_image_admin")


# ============================================================================ #


# ============================================================================ #
#                                 SETTING SITE                                 #
# ============================================================================ #


@seller_required
def setting_site_admin(request):
    setting = CommonInfo.objects.all()[:1]
    context = {"setting": setting}
    return render(
        request, "administration/setting_site/setting_site_admin.html", context
    )


# ============================================================================ #


@seller_required
def setting_site_create(request):
    if request.method == "POST":
        form = CommonInfoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Sozlamalar qoshildi")
            return redirect("setting_site_admin")
    else:
        form = CommonInfoForm()
    context = {"form": form}
    return render(
        request, "administration/setting_site/setting_site_create.html", context
    )


# ============================================================================ #


@seller_required
def setting_site_edit(request, pk):
    setting = CommonInfo.objects.get(pk=pk)
    if request.method == "POST":
        form = CommonInfoForm(request.POST, request.FILES, instance=setting)
        if form.is_valid():
            form.save()
            messages.success(request, "Sozlamalar yangilandi")
            return redirect("setting_site_admin")
    else:
        form = CommonInfoForm(instance=setting)
    context = {"form": form, "setting": setting}
    return render(
        request, "administration/setting_site/setting_site_edit.html", context
    )


# ============================================================================ #


@seller_required
def setting_site_delete(request, pk):
    setting = CommonInfo.objects.get(pk=pk)
    setting.delete()
    messages.success(request, "Sozlamalar o'chirildi")
    return redirect("setting_site_admin")


# ============================================================================ #
#                                CONTACT MESSAGE                               #
# ============================================================================ #


@seller_required
def contact_message_admin(request):
    contact_messages = ContactMessage.objects.all()
    contact_messages = paginate_queryset_admin(request, contact_messages)

    context = {
        "contact_messages": contact_messages,
    }
    return render(
        request, "administration/contact_message/contact_message_admin.html", context
    )


# ============================================================================ #


@seller_required
def contact_message_detail(request, pk):
    contact_message = ContactMessage.objects.get(pk=pk)
    if request.method == "POST":
        contact_message.status = request.POST.get("status")
        contact_message.save()
        return redirect("contact_message_admin")
    else:
        context = {
            "contact": contact_message,
        }
    contact_message.read = True
    contact_message.save()
    return render(
        request, "administration/contact_message/contact_message_detail.html", context
    )


# ============================================================================ #


@seller_required
def contact_message_delete(request, pk):
    contact_message = ContactMessage.objects.get(pk=pk)
    contact_message.delete()
    messages.success(request, "Malumotlaringiz o'chirildi ")
    return redirect("contact_message_admin")


# ============================================================================ #
#                               COLLECTION BOOKS                               #
# ============================================================================ #


CollectionFormset = inlineformset_factory(
    CollectionBook,
    CollectionSlider,
    fields=("collection", "image"),
    extra=2,
    can_delete=True,
    min_num=1,
    validate_min=True,
)


@seller_required
def collection_book_admin(request):
    collections = CollectionBook.objects.all()

    context = {"collections": collections}
    return render(request, "administration/collections/collections_admin.html", context)


# ============================================================================ #


@seller_required
def collection_book_create(request):
    collection = CollectionBook()

    if request.method == "POST":
        formset = CollectionFormset(
            request.POST or None,
            request.FILES or None,
            instance=collection,
            prefix="images",
        )
        form = CollectionBookForm(
            request.POST or None,
            request.FILES or None,
            instance=collection,
            prefix="collection",
        )
        if form.is_valid() and formset.is_valid():
            with transaction.atomic():
                form = form.save(commit=False)
                form.save()
                formset.save()
            messages.success(request, "Malumotlar qoshildi")
            return redirect("collection_book_admin")
    else:
        formset = CollectionFormset(instance=collection, prefix="images")
        form = CollectionBookForm(instance=collection, prefix="collection")
    context = {"form": form, "formset": formset}
    return render(
        request, "administration/collections/collections_create.html", context
    )


# ============================================================================ #


@seller_required
def collection_edit(request, pk):
    collection = CollectionBook.objects.get(pk=pk)
    if request.method == "POST":
        form = CollectionBookForm(
            request.POST or None,
            request.FILES or None,
            instance=collection,
            prefix="collection",
        )
        formset = CollectionFormset(
            request.POST or None,
            request.FILES or None,
            instance=collection,
            prefix="images",
            queryset=CollectionSlider.objects.filter(collection=collection),
        )

        if form.is_valid() and formset.is_valid():
            with transaction.atomic():
                form = form.save(commit=False)
                form.save()
                formset.save()
                messages.success(request, "Malumotlaringiz yangilandi")
                return redirect("collection_book_admin")
    else:
        form = CollectionBookForm(instance=collection, prefix="collection")
        formset = CollectionFormset(
            instance=collection,
            prefix="images",
            queryset=CollectionSlider.objects.filter(collection=collection),
        )

    form.fields["image"].widget.attrs["required"] = False

    context = {"form": form, "formset": formset, "collection": collection}
    return render(request, "administration/collections/collections_edit.html", context)


# ============================================================================ #


@seller_required
def collection_delete(request, pk):
    collection = CollectionBook.objects.filter(id=pk)
    collection.delete()
    messages.success(request, "Malumotlar o'chirildi")
    return redirect("collection_book_admin")


# ============================================================================ #


# ============================================================================ #
#                                      FAQ                                     #
# ============================================================================ #


@seller_required
def faq_admin(request):
    faqs = FAQ.objects.all()

    context = {"faqs": faqs}
    return render(request, "administration/faq/faq_admin.html", context)


# ============================================================================ #


@seller_required
def faq_create(request):
    if request.method == "POST":
        form = FaqForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Savollar qoshildi")
            return redirect("faq_admin")
    else:
        form = FaqForm()
    context = {"form": form}
    return render(request, "administration/faq/faq_create.html", context)


# ============================================================================ #


@seller_required
def faq_edit(request, pk):
    faq = FAQ.objects.get(pk=pk)
    if request.method == "POST":
        form = FaqForm(request.POST, instance=faq)
        if form.is_valid():
            form.save()
            messages.success(request, "Savollar yangilandi")
            return redirect("faq_admin")
    else:
        form = FaqForm(instance=faq)
    context = {"form": form, "faq": faq}
    return render(request, "administration/faq/faq_edit.html", context)


# ============================================================================ #


@seller_required
def faq_delete(request, pk):
    faq = FAQ.objects.get(pk=pk)
    faq.delete()
    messages.success(request, "Savollar o'chirildi")
    return redirect("faq_admin")


# ============================================================================ #


@seller_required
def about_admin(request):
    about_list = About.objects.all()

    context = {"about_list": about_list}
    return render(request, "administration/about/about_admin.html", context)


# ============================================================================ #


@seller_required
def about_create(request):
    if request.method == "POST":
        form = AboutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("about_admin")
    else:
        form = AboutForm()
    context = {"form": form}
    return render(request, "administration/about/about_create.html", context)


# ============================================================================ #


@seller_required
def about_edit(request, pk):
    about = About.objects.get(pk=pk)
    if request.method == "POST":
        form = AboutForm(request.POST, instance=about)
        if form.is_valid():
            form.save()
            return redirect("about_admin")
    else:
        form = AboutForm(instance=about)
    context = {"form": form, "about": about}
    return render(request, "administration/about/about_edit.html", context)


# ============================================================================ #


@seller_required
def about_delete(request, pk):
    about = About.objects.get(pk=pk)
    about.delete()
    return redirect("about_admin")


# ============================================================================ #


@seller_required
def shipping_info_admin(request):
    shipping_info_list = ShippingInfo.objects.all()

    context = {"shipping_info_list": shipping_info_list}
    return render(
        request, "administration/shipping_info/shipping_info_admin.html", context
    )


# ============================================================================ #


@seller_required
def shipping_info_create(request):
    if request.method == "POST":
        form = ShippingInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("shipping_info_admin")
    else:
        form = ShippingInfoForm()
    context = {"form": form}
    return render(
        request, "administration/shipping_info/shipping_info_create.html", context
    )


# ============================================================================ #


@seller_required
def shipping_info_edit(request, pk):
    shipping_info = ShippingInfo.objects.get(pk=pk)
    if request.method == "POST":
        form = ShippingInfoForm(request.POST, instance=shipping_info)
        if form.is_valid():
            form.save()
            return redirect("shipping_info_admin")
    else:
        form = ShippingInfoForm(instance=shipping_info)
    context = {"form": form, "shipping_info": shipping_info}
    return render(
        request, "administration/shipping_info/shipping_info_edit.html", context
    )


# ============================================================================ #


@seller_required
def shipping_info_delete(request, pk):
    shipping_info = ShippingInfo.objects.get(pk=pk)
    shipping_info.delete()
    return redirect("shipping_info_admin")


# ============================================================================ #


@seller_required
def payment_info_admin(request):
    payment_info_list = PaymentInfo.objects.all()

    context = {"payment_info_list": payment_info_list}
    return render(
        request, "administration/payment_info/payment_info_admin.html", context
    )


# ============================================================================ #


@seller_required
def payment_info_create(request):
    if request.method == "POST":
        form = PaymentInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("payment_info_admin")
    else:
        form = PaymentInfoForm()
    context = {"form": form}
    return render(
        request, "administration/payment_info/payment_info_create.html", context
    )


# ============================================================================ #


@seller_required
def payment_info_edit(request, pk):
    payment_info = PaymentInfo.objects.get(pk=pk)
    if request.method == "POST":
        form = PaymentInfoForm(request.POST, instance=payment_info)
        if form.is_valid():
            form.save()
            return redirect("payment_info_admin")
    else:
        form = PaymentInfoForm(instance=payment_info)
    context = {"form": form, "payment_info": payment_info}
    return render(
        request, "administration/payment_info/payment_info_edit.html", context
    )


# ============================================================================ #


@seller_required
def payment_info_delete(request, pk):
    payment_info = PaymentInfo.objects.get(pk=pk)
    payment_info.delete()
    return redirect("payment_info_admin")


# ============================================================================ #


@seller_required
def discount_info_admin(request):
    discount_info_list = DiscountInfo.objects.all()

    context = {"discount_info_list": discount_info_list}
    return render(
        request, "administration/discount_info/discount_info_admin.html", context
    )


# ============================================================================ #


@seller_required
def discount_info_create(request):
    if request.method == "POST":
        form = DiscountInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("discount_info_admin")
    else:
        form = DiscountInfoForm()
    context = {"form": form}
    return render(
        request, "administration/discount_info/discount_info_create.html", context
    )


# ============================================================================ #


@seller_required
def discount_info_edit(request, pk):
    discount_info = DiscountInfo.objects.get(pk=pk)
    if request.method == "POST":
        form = DiscountInfoForm(request.POST, instance=discount_info)
        if form.is_valid():
            form.save()
            return redirect("discount_info_admin")
    else:
        form = DiscountInfoForm(instance=discount_info)
    context = {"form": form, "discount_info": discount_info}
    return render(
        request, "administration/discount_info/discount_info_edit.html", context
    )


# ============================================================================ #


@seller_required
def discount_info_delete(request, pk):
    discount_info = DiscountInfo.objects.get(pk=pk)
    discount_info.delete()
    return redirect("discount_info_admin")