from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200, null= True)
    phone = models.CharField(max_length=300, null=True)
    email = models.CharField(max_length=300, null=True)
    date_created =models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return super().__str__()
    
    
class Tag(models.Model):
       name = models.CharField(max_length=200, null= True)
       
       def __str__(self) -> str:
        return super().__str__()
       
class Product(models.Model):
    
    CATEGORY = (
        ('In door', 'In door'),
        ('Out door', 'Out door'),
    )
    name = models.CharField(max_length=300, null=True)
    price = models.CharField(max_length=300, null=True)
    category = models.CharField(max_length=300, null=True, choices=CATEGORY)
    description =models.CharField(max_length=300, null=True,blank=True)
    date_created =models.DateTimeField(auto_now_add=True, null=True)
    tags =models.ManyToManyField(Tag)
    def __str__(self) -> str:
        return super().__str__()
    
class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery','Out for delivery'),
        ('Delivery', 'Delivery '),
        )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    date_create = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self) -> str:
        return super().__str__()
    
    