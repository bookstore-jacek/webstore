from django import forms   
from .models import Product

class UpdateForm(forms.Form):
    def __init__(self, request, product, *args, **kwargs):
        super(UpdateForm, self).__init__(*args, **kwargs)
        self.product = product
        self.fields['name'] = forms.CharField(label='', initial=self.product.name, required=False,  widget=forms.TextInput(attrs={ 'size': 16 }))
        self.fields['qt'] = forms.IntegerField(label='', initial=self.product.quantity, required=False,  widget=forms.NumberInput(attrs={ 'size': 16 }))
        self.fields['th'] = forms.IntegerField(label='', initial=self.product.threshold, required=False,  widget=forms.NumberInput(attrs={ 'size': 16 }))

    def clean_name(self, *args, **kwargs):
        raise forms.ValidationError('Produkt o podanej nazwie istnieje w bazie')
        name = self.cleaned_data.get('name')
        try:
            match = Product.objects.get(name__iexact=name)
        except Product.DoesNotExist:
            return name
        if match.id != self.product.id:
            raise forms.ValidationError('Produkt o podanej nazwie istnieje w bazie')
        else:
            return name

    def clean_qt(self, *args, **kwargs):
        qt = self.cleaned_data.get('qt')
        if qt < 0:
            raise forms.ValidationError('Ilość nie może być ujemna')
        return qt

    def clean_th(self, *args, **kwargs):
        th = self.cleaned_data.get('th')
        if th < 0:
            raise forms.ValidationError('Ilość nie może być ujemna')
        return th


class RaportForm(forms.Form):
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

class ProductSearchForm(forms.Form):
    user_input = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={ "placeholder":"Wpisz frazę", "class":"input_field"}))


class ProductForm(forms.ModelForm):
    name        =forms.CharField(label='', required=True, widget=forms.TextInput(attrs={ "placeholder":"Nazwa produktu *", "class":"input_field"}))
    quantity    =forms.CharField(label='', required=False, widget=forms.NumberInput(attrs={ "placeholder":"Aktualna ilość", "class":"input_field"}))
    threshold   =forms.CharField(label='', required=False, widget=forms.NumberInput(attrs={ "placeholder":"Próg dostępności", "class":"input_field"}))

    
    class Meta:
        model = Product
        fields = [
            'name',
            'quantity',
            'threshold',
        ]   
    

    def clean_name(self):

        name = self.cleaned_data.get('name')
        # Check to see if any users already exist with this email as a username.
        try:
            match = Product.objects.get(name=name)
        except Product.DoesNotExist:
            # Unable to find a user, this is fine
            return name

        # A user was found with this as a username, raise an error.
        raise forms.ValidationError('Wprowadzony produkt już istnieje.')

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity == "" :
            return '0'
        else:
            return quantity

    def clean_threshold(self):
        threshold = self.cleaned_data.get('threshold')
        if threshold == "" :
            return '0'
        else:
            return threshold

    def clean_name(self):
        return self.cleaned_data['name'].capitalize()