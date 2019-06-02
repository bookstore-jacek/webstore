from django.db import models

# Create your models here.
class Supplier(models.Model):
    name = models.CharField(unique=True, max_length=30)
    website = models.CharField(unique=True, max_length=30, blank=True, null=True)

    class Meta:
        db_table = 'supplier'