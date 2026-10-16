from django.conf import settings
from django.db import models

# expenses/models.py
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # your custom fields here
    pass


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique = True)
    slug = models.SlugField(max_length=100, unique = True)
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name



class PaymentType(models.Model):
    name = models.CharField(max_length=100, unique = True)
    slug = models.SlugField(max_length=100, unique = True)
    class Meta:
        verbose_name = 'PaymentType'
        verbose_name_plural = 'PaymentTypes'
        ordering = ['name']

    def __str__(self):
        return self.name



class Expense(models.Model):
    
    title = models.CharField(max_length=100)
    
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    author = models.CharField(max_length=100)

    
    payment_type = models.ForeignKey(PaymentType,
    on_delete=models.PROTECT,
    related_name = 'expenses',)


    category = models.ForeignKey(
    Category,
    on_delete=models.PROTECT,
    related_name = 'expenses',)


    author = models.ForeignKey(

        settings.AUTH_USER_MODEL ,
        on_delete = models.CASCADE,
        related_name='expenses',
            
          
     )


    class Meta:
        verbose_name = 'Expense'
        verbose_name_plural = 'Expenses'
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    
