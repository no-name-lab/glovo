from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractUser):
    ROLE_CHOICES = [
        ('client', 'Клиент'),
        ('courier', 'Курьер'),
        ('store_owner', 'Владелец магазина'),
        ('admin', 'Администратор'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    phone_number = PhoneNumberField(region='KG')

class Store(models.Model):
    store_name = models.CharField(max_length=100)
    description = models.TextField()
    contact = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stores')

    def __str__(self):
        return self.store_name

    def get_average_rating(self):
        reviews = self.reviews.all()
        if reviews.exists():
            return round(sum(review.stars for review in reviews) / reviews.count(), 1)
        return 0

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.product_name

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Ожидает'),
        ('in_progress', 'В процессе'),
        ('completed', 'Завершён'),
        ('canceled', 'Отменён'),
    ]
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    products = models.ManyToManyField(Product, related_name='orders')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    delivery_address = models.CharField(max_length=100)
    courier = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_orders')
    created_at = models.DateTimeField(auto_now_add=True)

class Courier(models.Model):
    STATUS_CHOICES = [
        ('available', 'Доступен'),
        ('busy', 'Занят'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    current_orders = models.ManyToManyField(Order, related_name='couriers', blank=True)

class Review(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='reviews')
    stars = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)], null=True, blank=False)
    comment = models.TextField()

    def __str__(self):
        return f"Review for {self.store.store_name} by {self.client.username}"
