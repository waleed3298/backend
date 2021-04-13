from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

### e-Commerce Options
CATEGORIES = (
    ('electric','ELECTRIC'),
    ('paints','PAINTS'),
    ('wallpapers', 'WALLPAPERS'),
    ('construction_tools', 'CONSTRUCTION_TOOLS'),
    ('building_material','BUILDING_MATERIAL'),
    ('bathroom','BATHROOM'),
    ('lighting','LIGHTING'),
    ('hardware','HARDWARE'),
    ('decor','DECOR'),
    ('security','SECURITY'),
    ('kitchen','KITCHEN'),
    ('walls_and_flooring','WALLS_AND_FLOORING'),
)



### Property Options
UNITS_CHOICES = (
    ('marla','MARLA'),
    ('kanal','KANAL'),
    ('square_meters', 'SQUARE_METERS'),
    ('square_yards', 'SQUARE_YARDS'),
)
TYPE_CHOICES = (
    ('property','PROPERTY'),
    ('plot', 'PLOT'),
    ('commercial', 'COMMERCIAL'),
    ('flat','FLAT'),
    ('penthouse','PENTHOUSE'),
)
STATUS_CHOICES = (
    ('complete','COMPLETE'),
    ('under_construction', 'UNDER_CONSTRUCTION'),
)
PURPOSE = (
    ('rent','RENT'),
    ('sale','SALE'),
)

class Ad(models.Model):
    Title = models.CharField(max_length=128)
    Description = models.TextField(null=True,blank=True)
    City = models.CharField(max_length=128,null=True)
    Location = models.CharField(max_length=256,null=True)
    Image = models.ImageField(default='media/api/images/house.png',null=True,blank=True, upload_to='media/api/images')
    Image1 = models.ImageField(default='media/api/images/random.png',null=True,blank=True, upload_to='media/api/images')
    Image2 = models.ImageField(default='media/api/images/random.png',null=True,blank=True, upload_to='media/api/images')
    Image3 = models.ImageField(default='media/api/images/random.png',null=True,blank=True, upload_to='media/api/images')
    Image4 = models.ImageField(default='media/api/images/random.png',null=True,blank=True, upload_to='media/api/images')
    Image5 = models.ImageField(default='media/api/images/random.png',null=True,blank=True, upload_to='media/api/images')
    Size = models.IntegerField()
    Units = models.CharField(max_length=128,choices=UNITS_CHOICES,default='MARLA')
    Beds = models.IntegerField()
    Baths = models.IntegerField()
    Price = models.IntegerField()
    Type = models.CharField(max_length=128,choices=TYPE_CHOICES,default='PROPERTY')
    Construction_status = models.CharField(max_length=128,choices=STATUS_CHOICES,default='COMPLETE')
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    Purpose = models.CharField(max_length=128,null=True,blank=True,choices=PURPOSE,default='sale')
    User = models.ForeignKey(User,on_delete=models.CASCADE)
    contact_no = models.IntegerField(null=True,blank=True)
    cell_no = models.IntegerField(null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    Time = models.DateTimeField(default=now,blank=True)
    Featured = models.BooleanField(default=False)
    Views = models.IntegerField(default=0)
    Additional_specifications = models.CharField(max_length=128,null=True)
    def __str__(self):
        return self.Title

class Saved(models.Model):
    Ad = models.ForeignKey(Ad,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Title = models.CharField(max_length=128,null=True)
    Price = models.IntegerField(null=True)
    Image = models.ImageField(default='media/api/images/house.png',null=True,blank=True, upload_to='media/api/images')
        
    class Meta:
        unique_together = (('user','Ad'),)
        index_together = (('user','Ad'),)
class PriceIndex(models.Model):
    City = models.CharField(max_length=128,blank=False,null=False)
    Price_to_income = models.FloatField(blank=True,null=True)
    Mortgage_interest_ratio = models.FloatField(blank=True,null=True)
    Price_to_rent = models.FloatField(blank=True,null=True)
    rental_yield = models.FloatField(blank=True,null=True)
    Price_per_sqr_mtr = models.FloatField(blank=True,null=True)
    
    def __str__(self):
        return self.City
class YearlyIndices(models.Model):
    City = models.CharField(max_length=128,blank=False,null=False)
    y_2013 = models.FloatField(blank=True,null=True)
    y_2014 = models.FloatField(blank=True,null=True)
    y_2015 = models.FloatField(blank=True,null=True)
    y_2016 = models.FloatField(blank=True,null=True)
    y_2017 = models.FloatField(blank=True,null=True)
    y_2018 = models.FloatField(blank=True,null=True)
    y_2019 = models.FloatField(blank=True,null=True)
    y_2020 = models.FloatField(blank=True,null=True)
    y_2021 = models.FloatField(blank=True,null=True)
    
    def __str__(self):
        return self.City
    
class Product(models.Model):
    User = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    Title = models.CharField(max_length=200, null=True, blank=True)
    Image = models.ImageField(null=True, blank=True,
                              default='/placeholder.png')
    Brand = models.CharField(max_length=200, null=True, blank=True)
    Category = models.CharField(max_length=200,choices=CATEGORIES,default="ELECTRIC")
    Description = models.TextField(null=True, blank=True)
    Price = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    countInStock = models.IntegerField(null=True, blank=True, default=0)
    CreatedAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def no_of_reviews(self):
        review = Review.objects.filter(Product=self)
        return len(review)
    
    def avg_rating(self):
        sum = 0
        ratings = Review.objects.filter(Product=self)
        for rating in ratings:
            sum+= rating.Rating
            
        if len(ratings)>0:
            avg = sum / len(ratings)
            return round(avg,1)
        else:
            return 0
 
    def __str__(self):
        return self.Title
    
class Review(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Name = models.CharField(max_length=200, null=True, blank=True)
    Rating = models.FloatField(null=True, blank=True, default=0)
    Comment = models.TextField(null=True, blank=True)
    CreatedAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.Product)
    
    class Meta:
        unique_together = (('user','Product'),)
        index_together = (('user','Product'),)
        
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    paymentMethod = models.CharField(max_length=200, null=True, blank=True)
    taxPrice = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    shippingPrice = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    totalPrice = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    isPaid = models.BooleanField(default=False)
    paidAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    isDelivered = models.BooleanField(default=False)
    deliveredAt = models.DateTimeField(
        auto_now_add=False, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.createdAt)
class OrderItem(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    Order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    Name = models.CharField(max_length=200, null=True, blank=True)
    Qty = models.IntegerField(null=True, blank=True, default=0)
    Price = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    Image = models.CharField(max_length=200, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)

class Blog(models.Model):
    Title = models.CharField(max_length=128,null=False,blank=False)
    Title_image = models.ImageField(default=None,null=True,blank=True, upload_to='media/api/images')
    content=models.TextField(null=False,blank=False)
    genre = models.CharField(max_length=128,null=False,blank=False,default=None)
    extra_image1 = models.ImageField(default=None,null=True,blank=True, upload_to='media/api/images')
    extra_image2 = models.ImageField(default=None,null=True,blank=True, upload_to='media/api/images')
    extra_image3 = models.ImageField(default=None,null=True,blank=True, upload_to='media/api/images')
    
class ShippingAddress(models.Model):
    Order = models.OneToOneField(
        Order, on_delete=models.CASCADE, null=True, blank=True)
    Address = models.CharField(max_length=200, null=True, blank=True)
    City = models.CharField(max_length=200, null=True, blank=True)
    PostalCode = models.CharField(max_length=200, null=True, blank=True)
    Country = models.CharField(max_length=200, null=True, blank=True)
    ShippingPrice = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.address)