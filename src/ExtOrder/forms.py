from django import forms   
from .models import ExtOrder as Order

class CustomerForm(forms.Form):
    text = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={ "placeholder":"Wyszukaj klienta *", "class": "input_field"}))

class CustomerRadioForm(forms.Form):
    def __init__(self, customers, *args, **kwargs):
        super(CustomerRadioForm, self).__init__(*args, **kwargs)
        CHOICES = [(cust.id, f"{cust.first_name} {cust.last_name}") for cust in customers[:8]]
        self.fields['choosen_customer'] = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, label='')

class ProductForm(forms.Form):
    text = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={ "placeholder":"Wyszukaj produkt *", "class": "input_field"}))

class ProductRadioForm(forms.Form):
    def __init__(self, products, *args, **kwargs):
        super(ProductRadioForm, self).__init__(*args, **kwargs)
        CHOICES = [(prod.id, prod.name) for prod in products[:8]]
        self.fields['choosen_product'] = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, label='')