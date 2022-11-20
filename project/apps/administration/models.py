from django.db import models
from django.contrib.auth import get_user_model

# ============================================================================ #

from project.apps.book.models import Book
from project.apps.common.models import BaseModel


User = get_user_model()


# ================================= SHOPCART ================================= #


class ShopCart(BaseModel):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="shopcart_user"
    )
    product = models.ForeignKey(
        Book, on_delete=models.SET_NULL, null=True, related_name="shopcart_product"
    )
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.title

    @property
    def price(self):
        return self.product.price

    @property
    def image(self):
        return self.product.coverpage

    def amount(self):
        return self.quantity * self.product.price
