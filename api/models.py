from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
import datetime
import json

### e-Commerce Options
CATEGORIES = (
    ("electric", "ELECTRIC"),
    ("paints", "PAINTS"),
    ("wallpapers", "WALLPAPERS"),
    ("construction_tools", "CONSTRUCTION_TOOLS"),
    ("building_material", "BUILDING_MATERIAL"),
    ("bathroom", "BATHROOM"),
    ("lighting", "LIGHTING"),
    ("hardware", "HARDWARE"),
    ("decor", "DECOR"),
    ("security", "SECURITY"),
    ("kitchen", "KITCHEN"),
    ("walls_and_flooring", "WALLS_AND_FLOORING"),
)


### Property Options
UNITS_CHOICES = (
    ("marla", "MARLA"),
    ("kanal", "KANAL"),
    ("square_meters", "SQUARE_METERS"),
    ("square_yards", "SQUARE_YARDS"),
)
TYPE_CHOICES = (
    ("property", "PROPERTY"),
    ("plot", "PLOT"),
    ("commercial", "COMMERCIAL"),
    ("flat", "FLAT"),
    ("penthouse", "PENTHOUSE"),
)
STATUS_CHOICES = (
    ("complete", "COMPLETE"),
    ("under_construction", "UNDER_CONSTRUCTION"),
)
PURPOSE = (
    ("rent", "RENT"),
    ("sale", "SALE"),
)

GENDER_CHOICES = (
    ("male", "MALE"),
    ("female", "FEMALE"),
)


class Profile(models.Model):
    Full_Name = models.CharField(max_length=128, null=False)
    Gender = models.CharField(max_length=128, choices=GENDER_CHOICES, default="MALE")
    Age = models.IntegerField(null=True)
    CNIC = models.IntegerField(null=True)
    Ad_quantity = models.IntegerField(null=False, default="4")
    User = models.ForeignKey(User, on_delete=models.CASCADE, null=False)


class Ad(models.Model):
    Title = models.CharField(max_length=128)
    Description = models.TextField(null=True, blank=True)
    City = models.CharField(max_length=128, null=True)
    Location = models.CharField(max_length=256, null=True)
    Image = models.ImageField(
        default="media/api/images/house.png",
        null=True,
        blank=True,
        upload_to="media/api/images",
    )
    Image1 = models.ImageField(
        default="media/api/images/random.png",
        null=True,
        blank=True,
        upload_to="media/api/images",
    )
    Image2 = models.ImageField(
        default="media/api/images/random.png",
        null=True,
        blank=True,
        upload_to="media/api/images",
    )
    Image3 = models.ImageField(
        default="media/api/images/random.png",
        null=True,
        blank=True,
        upload_to="media/api/images",
    )
    Image4 = models.ImageField(
        default="media/api/images/random.png",
        null=True,
        blank=True,
        upload_to="media/api/images",
    )
    Image5 = models.ImageField(
        default="media/api/images/random.png",
        null=True,
        blank=True,
        upload_to="media/api/images",
    )
    Size = models.IntegerField()
    Units = models.CharField(max_length=128, choices=UNITS_CHOICES, default="MARLA")
    Beds = models.IntegerField()
    Baths = models.IntegerField()
    Price = models.IntegerField()
    Type = models.CharField(max_length=128, choices=TYPE_CHOICES, default="PROPERTY")
    Construction_status = models.CharField(
        max_length=128, choices=STATUS_CHOICES, default="COMPLETE"
    )
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    Purpose = models.CharField(
        max_length=128, null=True, blank=True, choices=PURPOSE, default="sale"
    )
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Time = models.DateTimeField(default=now, blank=True)
    Featured = models.BooleanField(default=False)
    Views = models.IntegerField(default=0)
    Additional_specifications = models.CharField(max_length=128, null=True)

    def __str__(self):
        return self.Title

    def username(self):
        user = User.objects.filter(id=self.User.id)
        return user[0].username

    def email(self):
        user = User.objects.filter(id=self.User.id)
        return user[0].email


class Saved(models.Model):
    Ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Title = models.CharField(max_length=128, null=True)
    Price = models.IntegerField(null=True)
    Image = models.ImageField(
        default="media/api/images/house.png",
        null=True,
        blank=True,
        upload_to="media/api/images",
    )

    class Meta:
        unique_together = (("user", "Ad"),)
        index_together = (("user", "Ad"),)


class PriceIndex(models.Model):
    City = models.CharField(max_length=128, blank=False, null=False)
    Price_to_income = models.FloatField(blank=True, null=True)
    Mortgage_interest_ratio = models.FloatField(blank=True, null=True)
    Price_to_rent = models.FloatField(blank=True, null=True)
    rental_yield = models.FloatField(blank=True, null=True)
    Price_per_sqr_mtr = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.City


class YearlyIndices(models.Model):
    City = models.CharField(max_length=128, blank=False, null=False)
    y_2013 = models.FloatField(blank=True, null=True)
    y_2014 = models.FloatField(blank=True, null=True)
    y_2015 = models.FloatField(blank=True, null=True)
    y_2016 = models.FloatField(blank=True, null=True)
    y_2017 = models.FloatField(blank=True, null=True)
    y_2018 = models.FloatField(blank=True, null=True)
    y_2019 = models.FloatField(blank=True, null=True)
    y_2020 = models.FloatField(blank=True, null=True)
    y_2021 = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.City


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, default="/placeholder.png")
    brand = models.CharField(max_length=200, null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    countInStock = models.IntegerField(null=True, blank=True, default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name

    def no_of_reviews(self):
        review = Review.objects.filter(Product=self)
        return len(review)

    def avg_rating(self):
        sum = 0
        ratings = Review.objects.filter(Product=self)
        for rating in ratings:
            sum += rating.Rating

        if len(ratings) > 0:
            avg = sum / len(ratings)
            return round(avg, 1)
        else:
            return 0


class Review(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Name = models.CharField(max_length=200, null=True, blank=True)
    Rating = models.FloatField(null=True, blank=True, default=0)
    Comment = models.TextField(null=True, blank=True)
    CreatedAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    # def __str__(self):
    # return str(self.Product)

    class Meta:
        unique_together = (("user", "Product"),)
        index_together = (("user", "Product"),)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    paymentMethod = models.CharField(max_length=200, null=True, blank=True)
    taxPrice = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True
    )
    shippingPrice = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True
    )
    totalPrice = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True
    )
    isPaid = models.BooleanField(default=False)
    paidAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    isDelivered = models.BooleanField(default=False)
    deliveredAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    createdAtDate = models.DateField(default=datetime.date.today)
    createdAtTime = models.TimeField(auto_now_add=True, null=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.createdAtDate)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=128, null=True)
    qty = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    image = models.CharField(max_length=200, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.price)


class ShippingAddress(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    postalCode = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    shippingPrice = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True
    )
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.address)


class Blog(models.Model):
    Title = models.CharField(max_length=128, null=False, blank=False)
    Title_image = models.ImageField(
        default=None, null=True, blank=True, upload_to="media/api/images"
    )
    para0 = models.TextField(null=True, blank=True)
    para1 = models.TextField(null=True, blank=True)
    para2 = models.TextField(null=True, blank=True)
    para3 = models.TextField(null=True, blank=True)
    para4 = models.TextField(null=True, blank=True)
    para5 = models.TextField(null=True, blank=True)
    para6 = models.TextField(null=True, blank=True)
    para7 = models.TextField(null=True, blank=True)
    genre = models.CharField(max_length=128, null=False, blank=False, default=None)
    subheading1 = models.CharField(max_length=128, null=True, blank=True)
    subheading2 = models.CharField(max_length=128, null=True, blank=True)
    subheading3 = models.CharField(max_length=128, null=True, blank=True)
    subheading4 = models.CharField(max_length=128, null=True, blank=True)
    subheading5 = models.CharField(max_length=128, null=True, blank=True)
    subheading6 = models.CharField(max_length=128, null=True, blank=True)
    subheading7 = models.CharField(max_length=128, null=True, blank=True)
    extra_image1 = models.ImageField(
        default=None, null=True, blank=True, upload_to="media/api/images"
    )
    extra_image2 = models.ImageField(
        default=None, null=True, blank=True, upload_to="media/api/images"
    )
    extra_image3 = models.ImageField(
        default=None, null=True, blank=True, upload_to="media/api/images"
    )

    def __str__(self):
        return self.Title
