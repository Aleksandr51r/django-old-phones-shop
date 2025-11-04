from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
class Order(models.Model):
    User = get_user_model()
    order_number = models.UUIDField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    deleted_user_info = models.CharField(max_length=255, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    track_number = models.BooleanField(default=False)
    is_send = models.BooleanField(default=False)
    is_received = models.BooleanField(default=False)
    payment_status = models.CharField(
        max_length=20, choices=[("pending", "Pending"), ("paid", "Paid"), ("failed", "Failed")]
    )
    shipping_address = models.TextField(blank=True, null=False)
    notes = models.TextField(blank=True, null=True)