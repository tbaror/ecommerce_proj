from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.CharField(max_length=250, blank=True)
    image = models.ImageField(upload_to='catogery', blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'catogery'
        verbose_name_plural = 'catogeries'

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.CharField(max_length=250, blank=True)
    catogery = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='catogery', blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name

            