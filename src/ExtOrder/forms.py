from django import forms   
from .models import ExtOrder as Order
from Customer.models import Customer
from Product.models import Product

class OrderSearchForm(forms.Form):
    user_input = forms.CharField(label='', required=True,  widget=forms.TextInput(attrs={ "placeholder":"Wyszukaj frazę", "class":"input_field"}))
    status     = forms.ChoiceField(choices=(('all',    'Wszystkie'),
                                           ('unfinished', 'Niezakończone'),
                                           ('finished', 'Zakończone'),
                                           ('cancelled',  'Anulowane')))

class OrderForm(forms.Form):
    phone     = forms.CharField(label='', required=True,  widget=forms.TextInput(attrs={ "placeholder":"Numer telefonu *",       "class":"input_field"}))
    product1  = forms.CharField(label='', required=True,  widget=forms.TextInput(attrs={ "placeholder":"Produkt *",              "class":"input_field"}))
    product2  = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={ "placeholder":"(opcjonalne) Produkt", "class":"input_field"}))
    product3  = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={ "placeholder":"(opcjonalne) Produkt", "class":"input_field"}))
    product4  = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={ "placeholder":"(opcjonalne) Produkt", "class":"input_field"}))
    product5  = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={ "placeholder":"(opcjonalne) Produkt", "class":"input_field"}))
    paid      = forms.ChoiceField(choices=(('not_paid',    'Nieopłacone'),
                                           ('partly_paid', 'Wpłacono zaliczkę'),
                                           ('fully_paid',  'Opłacone')))

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not (len(phone) == 9 or len(phone) == 12):
            raise forms.ValidationError('Wprowadzony numer jest nieprawidłowy')
        try:
            match = Customer.objects.get(phone=phone)
        except Customer.DoesNotExist:
            raise forms.ValidationError('Klient z podanym numerem nie istnieje')
        return match

    def clean_product1(self):
        product = self.cleaned_data.get('product1')
        if product == "":
            raise forms.ValidationError('Pole wymagane')
        try:
            match = Product.objects.get(name__iexact=product)
        except Product.DoesNotExist:
            raise forms.ValidationError('Podany produkt nie istnieje')
        return match

    def clean_product2(self):
        product = self.cleaned_data.get('product2')
        if product == "":
            return None
        try:
            match = Product.objects.get(name__iexact=product)
        except Product.DoesNotExist:
            raise forms.ValidationError('Podany produkt nie istnieje')
        return match

    def clean_product3(self):
        product = self.cleaned_data.get('product3')
        if product == "":
            return None
        try:
            match = Product.objects.get(name__iexact=product)
        except Product.DoesNotExist:
            raise forms.ValidationError('Podany produkt nie istnieje')
        return match

    def clean_product4(self):
        product = self.cleaned_data.get('product4')
        if product == "":
            return None
        try:
            match = Product.objects.get(name__iexact=product)
        except Product.DoesNotExist:
            raise forms.ValidationError('Podany produkt nie istnieje')
        return match

    def clean_product5(self):
        product = self.cleaned_data.get('product5')
        if product == "":
            return None
        try:
            match = Product.objects.get(name__iexact=product)
        except Product.DoesNotExist:
            raise forms.ValidationError('Podany produkt nie istnieje')
        return match

    def clean_paid(self):
        return self.cleaned_data.get('paid')