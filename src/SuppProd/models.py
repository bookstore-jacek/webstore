from django.db import models
from Product.models import Product

# Create your models here.
class SuppProd(models.Model):
    product = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)
    supplier = models.ForeignKey('Supplier', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'supp_prod'