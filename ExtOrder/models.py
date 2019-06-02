from django.db import models
from Customer.models import Customer

# Create your models here.
class ExtOrder(models.Model):
    customer = models.ForeignKey(Customer, models.DO_NOTHING, blank=True, null=True)
    paid = models.TextField()  # This field type is a guess.
    submitted = models.DateTimeField()
    finished = models.DateTimeField(blank=True, null=True)
    cancelled = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'ext_order'