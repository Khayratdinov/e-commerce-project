from django.db import models
from django.contrib.auth import get_user_model

# ============================================================================ #
from project.apps.book.models import Book, CollectionBook
from project.apps.common.models import BaseModel

# =================================== ORDER ================================== #
User = get_user_model()

# ================================= SHIPPING ================================= #


class Shipping(BaseModel):
    title = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    wight = models.DecimalField(max_digits=10, decimal_places=3)

    class Meta:
        verbose_name = "2. Yetkazip beruvshi"
        verbose_name_plural = "2. Yetkazip beruvshilar"

    def __str__(self):
        return self.title


# =================================== ORDER ================================== #


class Order(BaseModel):
    STATUS = (
        ("New", "Yangi"),
        ("Accepted", "Qabul qilindi"),
        ("Preparing", "Tayyorlanmoqda"),
        ("OnShipping", "Buyurtma yo'lda"),
        ("Completed", "Buyurtma yetkazib berildi"),
        ("Canceled", "Buyurtma bekor qilindi"),
    )

    PAYMENT_METHOT = (
        ("NAQD", "NAQD"),
        ("CLICK", "CLICK"),
        ("PAYME", "PAYME"),
        ("CANCELED", "Bekor qilingan"),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    street_address_1 = models.CharField(max_length=40, blank=False)
    street_address_2 = models.CharField(max_length=40, blank=False)
    order_code = models.CharField(max_length=8, editable=False)
    shipping = models.ForeignKey(
        Shipping, on_delete=models.CASCADE, blank=True, null=True
    )
    status = models.CharField(max_length=30, choices=STATUS, default="New")
    payment_methot = models.CharField(
        max_length=10, choices=PAYMENT_METHOT, default="NAQD"
    )
    is_paid = models.BooleanField(default=False)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    offline_sales = models.BooleanField(default=False)
    collection_order = models.BooleanField(default=False)
    ip = models.CharField(blank=True, max_length=30, null=True)

    class Meta:
        verbose_name = "1. Buyirtma"
        verbose_name_plural = "1. Buyirtmalar"

    def __str__(self):
        return self.full_name


# =============================== ORDERLINEITEM ============================== #


class OrderLineItem(BaseModel):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="order_item",
    )
    product = models.ForeignKey(
        Book, on_delete=models.CASCADE, blank=True, null=True, related_name="order_item"
    )
    quantity = models.IntegerField(blank=True, null=True, default=0)
    collection_book = models.ForeignKey(
        CollectionBook,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="order_item",
    )
    collection_order_status = models.BooleanField(default=False)

    @property
    def get_price(self):
        return int(self.product.get_discount_price * int(self.quantity))

    @property
    def get_collection_price(self):
        return int(self.collection_book.price * int(self.quantity))

    class Meta:
        verbose_name = "3. Buyirtma savatchasi"
        verbose_name_plural = "3. Buyirtma savatchasi"