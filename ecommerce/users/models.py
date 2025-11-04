from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class CommercialInfo(models.Model):
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    email_verified = models.BooleanField(default=False)
    phone_verified = models.BooleanField(default=False)
    profile_icon = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

    class Meta:
        abstract = True


class User(AbstractUser, CommercialInfo):
    ROLE_CHOICES = [
        ('buyer', 'Buyer'),
        ('seller', 'Seller'),
        ('admin', 'Admin'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='buyer')
    birth_date = models.DateField(blank=True, null=True)
    shop_name = models.CharField(max_length=255, blank=True, null=True)     # ?
    shop_description = models.TextField(blank=True, null=True)              # ?
    iban = models.CharField(max_length=34, blank=True, null=True)

    def __str__(self):
        if self.role == "seller" and self.shop_name:
            return self.shop_name
        return self.username


class ShopProfile(CommercialInfo):
    user = models.OneToOneField('User', on_delete=models.CASCADE, related_name="shop_profile")
    shop_name = models.CharField(max_length=255, blank=True, null=True)
    shop_description = models.TextField(blank=True, null=True)
    iban = models.CharField(max_length=34, blank=True, null=True)

    def __str__(self):
        return self.shop_name or f"Shop of {self.user.username}"




