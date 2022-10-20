from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect, JsonResponse
from django.utils.translation import gettext as _


# ============================================================================ #
from project.apps.cart.cart import Cart
from project.apps.cart.forms import CartAddBookForm
from project.apps.book.models import Book


# ============================================================================ #
#                                     CART                                     #
# ============================================================================ #


# ================================ CART DETAIL =============================== #


def cart_detail(request):
    cart = Cart(request)

    context = {
        "cart": cart,
    }
    return render(request, "order/cart_detail.html", context)


# ================================= ADD CART ================================= #


@require_POST
def cart_add(request, book_id):
    url = request.META.get("HTTP_REFERER")
    cart = Cart(request)
    book = get_object_or_404(Book, id=book_id)
    form = CartAddBookForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(book=book, quantity=cd["quantity"], update_quantity=cd["update"])

    if request.POST.get("fast") == "1":
        return redirect("checkout")
    else:
        return HttpResponseRedirect(url)


# ================================ REMOVE CART =============================== #


def cart_remove(request, book_id):
    url = request.META.get("HTTP_REFERER")
    cart = Cart(request)
    book = get_object_or_404(Book, id=book_id)
    cart.remove(book)
    return HttpResponseRedirect(url)


# ================================ CART UPDATE =============================== #


def cart_update(request):
    book_id = int(request.GET.get("id", None))
    quantity = int(request.GET.get("quantity", None))
    url = request.META.get("HTTP_REFERER")
    cart = Cart(request)
    book = get_object_or_404(Book, id=book_id)
    cart.add(book, quantity, True)
    data = {"updated": True}
    return JsonResponse(data)
