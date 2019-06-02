from django.db import models
from ExtOrder.models import ExtOrder

# Create your models here.
class OrderedProduct(models.Model):
    order = models.ForeignKey(ExtOrder, models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey('Product.Product', models.DO_NOTHING, blank=True, null=True)
    ordered = models.DateTimeField(blank=True, null=True)
    collected = models.DateTimeField(blank=True, null=True)
    finished = models.DateTimeField(blank=True, null=True)
    cancelled = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'ordered_product'