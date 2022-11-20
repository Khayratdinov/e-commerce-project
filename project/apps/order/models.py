from django.db import models
from django.contrib.auth import get_user_model

# ============================================================================ #
from project.apps.book.models import Book
from project.apps.common.models import BaseModel

# =================================== ORDER ================================== #
User = get_user_model()

# ================================= SHIPPING ================================= #


class Shipping(BaseModel):
    title = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    wight = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self):
        return self.title


# =================================== ORDER ================================== #


class Order(BaseModel):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Preparing', 'Preparing'),
        ('OnShipping', 'OnShipping'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled'),
    )

    PAYMENT_METHOT = (

        ('NOT', 'NOT'),
        ('CLICK', 'CLICK'),
        ('PAYME', 'PAYME'),
        ('CANCELED', 'CANCELED'),
    )
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    street_address_1 = models.CharField(max_length=40, blank=False)
    street_address_2 = models.CharField(max_length=40, blank=False)
    date = models.DateField()
    order_code = models.CharField(max_length=8, editable=False)
    shipping = models.ForeignKey(
        Shipping, on_delete=models.CASCADE, blank=True, null=True
    )
    status = models.CharField(max_length=10,choices=STATUS,default='New')
    payment_methot = models.CharField(max_length=10,choices=PAYMENT_METHOT, default='NOT')
    is_paid = models.BooleanField(default=False)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    offline_sales = models.BooleanField(default=False)
    ip = models.CharField(blank=True, max_length=30,null=True)

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)


# =============================== ORDERLINEITEM ============================== #


class OrderLineItem(BaseModel):
    order = models.ForeignKey(Order, null=False, on_delete=models.CASCADE)
    product = models.ForeignKey(Book, null=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1} @ {2}".format(
            self.quantity, self.product.name, self.product.price
        )
