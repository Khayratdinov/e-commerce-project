from django.shortcuts import render

# ============================================================================ #
from project.apps.cart.cart import Cart
from project.apps.order.models import Shipping
from project.apps.common.models import HeadImages

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
