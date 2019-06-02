from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(unique=True, max_length=13)
    email = models.CharField(unique=True, max_length=30, blank=True, null=True)
    passhash = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'customer'