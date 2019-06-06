from django import forms
from Product.models import Product

class StockForm(forms.Form):
    name = forms.CharField(label='', required=True,  widget=forms.TextInput(attrs={ "placeholder":"Nazwa produktu *", "class":"input_field"}))
    qt   = forms.IntegerField(label='', required=True,  widget=forms.NumberInput(attrs={ "placeholder":"Ilość *", "class":"input_field"}))

    def clean_name(self, *args, **kwargs):
        name = self.cleaned_data.get('name')
        try:
            match = Product.objects.get(name__iexact=name)
        except Product.DoesNotExist:
            raise forms.ValidationError('Podany produkt nie istnieje')
        return match

    def clean_qt(self, *args, **kwargs):
        qt = self.cleaned_data.get('qt')
        if qt < 0:
            raise forms.ValidationError('Nie można zaktualizować o ujemną wartość')
        return qt