from django.shortcuts import render
from django.db.models.functions import Now
from .forms import StockForm
from .models import OrderedProduct
from Product.models import Product
from Customer.utils import sort_id 


# Create your views here.
def stock_update_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            prod = form.cleaned_data.get('name')
            qt = form.cleaned_data.get('qt')
            ordered = list(OrderedProduct.objects.filter(product_id=prod.id))
            ordered.sort(key=sort_id)
            for i in range(qt):
                if i == len(ordered):
                    break
                ordered[i].collected = Now()
                ordered[i].save()
            if qt > len(ordered):
                product = Product.objects.get(id=prod.id)
                product.quantity += qt
                product.save()
            form = StockForm()
    else:
        form = StockForm()

    context={
        "form": form
    }
    return render(request, "ord_prod/stock_update.html", context)