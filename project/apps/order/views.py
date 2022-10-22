from django.shortcuts import render, redirect
from django.conf import settings
import random

# ============================================================================ #
from project.apps.cart.cart import Cart
from project.apps.order.models import Shipping, Order, OrderLineItem
from project.apps.common.models import HeadImages
from project.apps.book.models import Book

# Create your views here.


def checkout(request):
    cart = Cart(request)
    shipping = Shipping.objects.all()
    bradcaump_img = HeadImages.objects.filter(status=True).order_by("?")[:1]

    context = {
        "cart": cart,
        "shipping": shipping,
        "bradcaump_img": bradcaump_img,
    }
    return render(request, "order/checkout.html", context)


def order_create(request):
    data = request.POST
    code = str(random.randint(10000000, 99999999))
    total = 0
    order = Order.objects.create(
        full_name=data["full_name"],
        phone_number=data["phone_number"],
        country=data["country"],
        postcode=data["postcode"],
        street_address_1=data["street_address_1"],
        street_address_2=data["street_address_2"],
        order_code=code,
        shipping=data["shipping"],
    )
    order.save()
    cart = request.session[settings.CART_SESSION_ID]
    for c in cart:
        book = Book.objects.get(pk=int(c))
        quantity = int(cart[c]["quantity"])
        price = float(cart[c]["price"])
        amount = quantity * price
        op = OrderLineItem.objects.create(
            order=order, product=book, quantity=quantity, price=price, amount=amount
        )
        total += int(cart[c]["quantity"]) * float(cart[c]["price"])
        op.save()
    if data["shipping"] != None:
        total += data["shipping"].price
    order.total = total
    order.save()
    cart = Cart(request)
    cart.clear()
    request.session["order_code"] = order.code

    return redirect("order_detail", order.code)


def order_detail(request, code):

    order = Order.objects.get(code=code)
    ret_url = request.META.get("HTTP_REFERER")
    order_code = order.code
    order_amount = order.total
    context = {
        "order": order,
    }
    return render(request, "order/order_detail.html", context)
