from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product_table(models.Model):


    cat = (

        ("Fashion", "Fashion"),
        ("Smart Phones", "Smart Phones"),
        ("Electronics", "Electronics"),
        ("Electrical Tools", "Electrical Tools"),
        ("Cars", "Cars"),
        ("Motor Bikes", "Motor Bikes"),
    )


    product_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=False)
    product_name = models.CharField(unique=True, max_length=50)
    date_upload = models.DateTimeField(auto_now_add=True, unique=False)
    quantity = models.IntegerField(unique=False, null=False)
    price = models.IntegerField(unique=False, null=False)
    description = models.CharField(unique=False, max_length=500, null=False)
    product_picture = models.ImageField(upload_to='productImage/', unique=True, null=True)
    category = models.CharField(max_length=20, choices=cat, default=None)
    approved = models.CharField(unique=False, max_length=10, null=True, default="Upa")
