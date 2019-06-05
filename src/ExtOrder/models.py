from django.db import models
from Customer.models import Customer
from django.urls import reverse

# Create your models here.
class ExtOrder(models.Model):
    customer  = models.ForeignKey(Customer, models.DO_NOTHING, blank=True)
    paid      = models.TextField()
    submitted = models.DateTimeField()
    finished  = models.DateTimeField(blank=True, null=True)
    cancelled = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'ext_order'

    def get_absolute_url(self):
        return reverse("zamowienie:order-detail/",kwargs={"id":self.id})