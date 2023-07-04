import random

from datetime import timedelta

# ============================================================================ #
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings

# ============================================================================ #
from clickuz import ClickUz
from clickuz.views import ClickUzMerchantAPIView

from paycomuz.views import MerchantAPIView
from paycomuz import Paycom
from decimal import Decimal

# ============================================================================ #
from project.apps.cart.cart import Cart
from project.apps.order.models import Shipping, Order, OrderLineItem
from project.apps.book.models import Book, CollectionBook
from project.apps.administration.models import ShopCart
from project.apps.users.models import CustomUser
from .telegram_bot import message_for_developer, send_order_to_telegram

# ============================================================================ #


def checkout(request):
    cart = Cart(request)
    shipping = Shipping.objects.all()

    context = {
        "cart": cart,
        "shipping": shipping,
    }
    return render(request, "order/checkout.html", context)


def collection_checkout(request, collection_id):
    collection_book = CollectionBook.objects.get(id=collection_id)
    shipping = Shipping.objects.all()

    context = {
        "collection_book": collection_book,
        "shipping": shipping,
    }

    return render(request, "order/checkout_collection.html", context)


def order_create(request):
    data = request.POST
    shipping = int(data.get("shipping", 0))
    code = str(random.randint(10000000, 99999999))

    user = data.get("user_id")

    if user:
        user = CustomUser.objects.get(id=user)
    else:
        user = None

    request.session.pop("order_code", None)
    request.session["order_code"] = code
    request.session.set_expiry(timedelta(minutes=10))

    total = 0

    if data.get("collection") == "1":
        collection_id = int(data.get("collection_id"))
        collection_book = CollectionBook.objects.filter(pk=collection_id).first()
        collection_order_status = True
        ship = Shipping.objects.filter(pk=shipping).first()

        order = Order.objects.create(
            user=user,
            full_name=data.get("full_name"),
            phone_number=data.get("phone_number"),
            country=data.get("country"),
            street_address_1=data.get("street_address_1"),
            street_address_2=data.get("street_address_2"),
            order_code=code,
            shipping=ship,
            collection_order=collection_order_status,
        )

        order_line_item = OrderLineItem.objects.create(
            order=order, collection_book=collection_book, collection_order_status=True
        )
        total = collection_book.price
        if ship:
            total += ship.price
        order.total = total
        order.save()
    elif data.get("collection") == "0":
        ship = Shipping.objects.filter(pk=shipping).first()

        order = Order.objects.create(
            user=user,
            full_name=data.get("full_name"),
            phone_number=data.get("phone_number"),
            country=data.get("country"),
            street_address_1=data.get("street_address_1"),
            street_address_2=data.get("street_address_2"),
            order_code=code,
            shipping=ship,
            collection_order=False,
        )

        cart = request.session.get(settings.CART_SESSION_ID, {})
        for c in cart:
            book = Book.objects.filter(pk=int(c)).first()
            quantity = int(cart[c].get("quantity", 0))
            op = OrderLineItem.objects.create(
                order=order, product=book, quantity=quantity
            )
            total += quantity * float(cart[c].get("price", 0))
            op.save()
        if ship:
            total += ship.price

        order.total = total
        order.save()
        cart = Cart(request)
        cart.clear()

    return redirect("order_detail", order.order_code)


# ============================================================================ #
def order_detail(request, code):
    paycom = Paycom()
    order = Order.objects.get(order_code=code)
    order_code = order.order_code
    order_amount = order.total

    click_link = ClickUz.generate_url(
        order_id=order_code,
        amount=str(order_amount),
        return_url="https://hamrohbooks.uz/successfully_payment_payme",
    )

    payme_link = paycom.create_initialization(
        amount=order_amount * 100,
        order_id=order_code,
        return_url="https://hamrohbooks.uz/successfully_payment_payme",
    )

    context = {"order": order, "click_link": click_link, "payme_link": payme_link}
    return render(request, "order/order_detail.html", context)


class OrderCheckAndPayment(ClickUz):
    def check_order(self, order_id: str, amount: str):
        orders = Order.objects.get(order_code=order_id)

        if order_id == orders.order_code and amount == str(int(orders.total)):
            return self.ORDER_FOUND
        elif order_id == orders.order_code and amount != str(int(orders.total)):
            orders.payment_methot = "CLICK"
            orders.status = "CANCELED"
            orders.save()
            return self.INVALID_AMOUNT

        else:
            orders.payment_methot = "CLICK"
            orders.status = "CANCELED"
            orders.save()
            return self.ORDER_NOT_FOUND

    def successfully_payment(self, order_id: str, transaction: object):
        orders = Order.objects.get(order_code=order_id)
        orders.payment_methot = "CLICK"
        orders.is_paid = True
        orders.save()


class ClickUzView(ClickUzMerchantAPIView):
    VALIDATE_CLASS = OrderCheckAndPayment


def successfully_payment_order_cash(request, code):
    order = get_object_or_404(
        Order.objects.prefetch_related("order_item"), order_code=code
    )
    order.payment_method = "NAQD"
    order.status = "New"
    order.is_paid = True
    order.save()
    send_order_to_telegram(order)

    return render(
        request, "order/successfully_payment_order_cash.html", {"order": order}
    )


# ============================================================================ #


# ================================= PAYME UZ ================================= #


class CheckOrder(Paycom):
    def check_order(self, amount, account, *args, **kwargs):
        amount = amount / 100
        order_code = account["order_id"]
        orders = Order.objects.get(order_code=order_code)

        if orders:
            order_total = orders.total
            if amount != Decimal(order_total):
                return self.INVALID_AMOUNT
            else:
                return self.ORDER_FOUND
        else:
            return self.ORDER_NOT_FOND

    def successfully_payment(self, account, transaction, *args, **kwargs):
        order_id = transaction.order_key
        orders = Order.objects.get(order_code=order_id)
        orders.payment_methot = "PAYME"
        orders.is_paid = True
        orders.save()

    def cancel_payment(self, account, transaction, *args, **kwargs):
        order_id = transaction.order_key
        orders = Order.objects.get(order_code=order_id)
        orders.payment_methot = "CANCELED"
        orders.payment_methot = "PAYME"
        orders.save()


class PaymeUzView(MerchantAPIView):
    VALIDATE_CLASS = CheckOrder


def successfully_payment_payme(request):
    if "order_code" in request.session:
        order_code = request.session["order_code"]
        order = get_object_or_404(
            Order.objects.prefetch_related("order_item"), order_code=order_code
        )
        send_order_to_telegram(order)
    else:
        order = 0

    context = {"order": order}
    return render(request, "order/successfully_payment_order_cash.html", context)