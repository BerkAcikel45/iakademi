from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    Category = (
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor'),
        ('Electronic', 'Electronic'),
    )
    name = models.CharField(max_length=250, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=250, null=True, choices=Category)
    description = models.CharField(max_length=500, null=True)
    dateCreated = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, null=True)
    phone = models.CharField(max_length=250, null=True)
    email = models.EmailField(max_length=200, null=True)
    dateCreated = models.DateTimeField(auto_now_add=True)
    profilePicture = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    Status = (
        ('Pending', 'Pending'),
        ('Out of Delivery', 'Out of Delivery'),
        ('Delivered', 'Delivered'),
    )
    # one to many
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=200, null=True, choices=Status)
    name = models.CharField(max_length=250, null=True)
    note = models.CharField(max_length=250, null=True)
    dateCreated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + " " + self.customer.name + " " + self.product.name