from django.db import models
from django.urls import reverse


class Brand(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    brand_logo = models.FileField(upload_to='brands/')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    name = models.CharField(max_length=255, db_index=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    release_year = models.PositiveIntegerField(blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
    tags = models.ManyToManyField('Tag', blank=True, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


def get_brand_image_path(instance, filename):
    return f'products/{instance.product.brand.name}/{filename}'


class PhoneSpecs(models.Model):
    product = models.OneToOneField(
        Product, on_delete=models.CASCADE, related_name='specs')
    network_type = models.CharField(max_length=50)
    battery = models.PositiveIntegerField(help_text="mAh")
    screen_size = models.DecimalField(
        max_digits=4, decimal_places=2, help_text="inches")
    screen_type = models.CharField(max_length=50, blank=True, null=True)
    resolution = models.CharField(max_length=20, blank=True, null=True)
    colors = models.PositiveIntegerField(blank=True, null=True)
    weight = models.PositiveIntegerField(
        blank=True, null=True, help_text="grams")
    dimensions = models.CharField(max_length=50, blank=True, null=True)
    sim_type = models.CharField(max_length=20, blank=True, null=True)
    sim_slots = models.PositiveIntegerField(default=1)

    memory_internal = models.CharField(max_length=50, blank=True, null=True)
    memory_card_support = models.BooleanField(default=False)

    has_sms = models.BooleanField(default=True)
    has_mms = models.BooleanField(default=False)
    has_infrared = models.BooleanField(default=False)
    has_bluetooth = models.BooleanField(default=False)
    has_wap = models.BooleanField(default=False)
    has_gprs = models.BooleanField(default=False)
    has_camera = models.BooleanField(default=False)
    has_radio = models.BooleanField(default=False)
    has_mp3 = models.BooleanField(default=False)
    has_games = models.BooleanField(default=False)
    java_support = models.BooleanField(default=False)

    form_factor = models.CharField(max_length=20, blank=True, null=True)
    ringtones = models.CharField(max_length=50, blank=True, null=True)


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='images')
    alt_text = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to=get_brand_image_path)
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return self.product.name


class Tag(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    description = models.TextField(blank=True, null=True)
    parent_category = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True, related_name='subcategories'
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
