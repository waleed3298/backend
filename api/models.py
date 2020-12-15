from django.db import models
from django.contrib.auth.models import User

UNITS_CHOICES = (
    ('marla','MARLA'),
    ('kanal','KANAL'),
    ('square_feet', 'SQUARE_FEET'),
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

class Profile(models.Model):
    username = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    contact_no = models.IntegerField(null=True)
    password = models.CharField(max_length=128)
    
    def __str__(self):
        return self.email

class Ad(models.Model):
    Title = models.CharField(max_length=128)
    Description = models.TextField(null=True,blank=True)
    City = models.CharField(max_length=128,null=True)
    Location = models.CharField(max_length=256,null=True)
    Image = models.ImageField(default='media/api/images/house.png',null=True,blank=True, upload_to='media/api/images')
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

    def __str__(self):
        return self.Title
