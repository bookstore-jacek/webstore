from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.IntegerField(blank=True, default=0)
    threshold = models.IntegerField(blank=True, default=0)

    class Meta:
        db_table = 'product'