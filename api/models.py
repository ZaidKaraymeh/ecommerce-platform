from django.db import models
# Create your models here.
import uuid
from decimal import Decimal
from django.core.validators import MaxValueValidator, MinValueValidator


class Shop(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    owner = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE)
    
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=13)
    picture = models.ImageField(upload_to='pictures', blank=True)
    about = models.TextField(max_length=9000)


    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name
    


class Product(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    owner = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE)
    shop = models.ForeignKey("api.Shop", on_delete=models.CASCADE, null=True)

    name = models.CharField(max_length=255)
    description = models.TextField(max_length=9000)
    picture = models.ImageField(upload_to='pictures', blank=True)
    price = models.DecimalField(
        max_digits=6, decimal_places=3, default=Decimal(0))

    rating_average = models.DecimalField(max_digits=2, decimal_places=1, default=0,
                                         validators=[
                                             MaxValueValidator(5),
                                             MinValueValidator(0)
                                         ])
    rating_count = models.IntegerField(default=0)
    coupon = models.IntegerField(default=0,
                                 validators=[
                                     MaxValueValidator(100),
                                     MinValueValidator(0)
                                 ])
    """
        Check if user found in users_rated, 
        if user not in users_rated, 
            call add_new_average
            increment rating_count
            update rating_average
        else:
            get old rating
            call subtract_new_average
            decrement rating_count
            update rating_average

            call add_new_average with new value
            increment rating_count
            update rating_average

    """

    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name
    


class UserRating(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    product = models.ForeignKey("api.Product", on_delete=models.CASCADE, null=True)
    
    rating = models.IntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ])


    comment = models.TextField(max_length=500, null=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

class ProductOrder(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    shop = models.ForeignKey("api.Shop", related_name="shop", on_delete=models.CASCADE)
    owner = models.ForeignKey("users.CustomUser", related_name="owner",on_delete=models.CASCADE)

    customer = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    products = models.ManyToManyField("api.Product")

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)