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
    Image1 = models.ImageField(null=True,blank=True, upload_to='media/api/images')
    Image2 = models.ImageField(null=True,blank=True, upload_to='media/api/images')
    Image3 = models.ImageField(null=True,blank=True, upload_to='media/api/images')
    Image4 = models.ImageField(null=True,blank=True, upload_to='media/api/images')
    Image5 = models.ImageField(null=True,blank=True, upload_to='media/api/images')
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

class ItemAD(models.Model):
    Title = models.CharField(max_length=128)
    Image = models.ImageField(default='media/api/images/tools.png',null=True,blank=True, upload_to='media/api/images')
    Description = models.TextField(null=True)
    Price = models.IntegerField()
    Discounted_Price = models.IntegerField(null=True)
    Category = models.CharField(max_length=128,choices=CATEGORIES,default='construction_tools')
    Type = models.CharField(max_length=128)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Additional_specifications = models.CharField(max_length=128,null=True)
    
    def __str__(self):
        return self.Title