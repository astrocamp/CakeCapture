from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg

import datetime

import datetime


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, decimal_places=1, max_digits=100)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, default=1, related_name="items"
    )
    quantity = models.IntegerField(default=0)
    description = models.CharField(max_length=100, default="", blank=True, null=True)
    image = models.ImageField(upload_to="uploads/product/")

    def __str__(self):
        return self.name

    def average_rating(self):
        avg_rating = self.reviews.aggregate(Avg("rating"))["rating__avg"]
        return avg_rating


RATING = (
    (1, "★☆☆☆☆"),
    (2, "★★☆☆☆"),
    (3, "★★★☆☆"),
    (4, "★★★★☆"),
    (5, "★★★★★"),
)


class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, related_name="reviews"
    )
    review = models.TextField()
    rating = models.IntegerField(choices=RATING, default=None)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Product Reviews"

    def __str__(self):
        return self.product.name

    def get_rating(self):
        return self.rating
