from django import forms   
from .models import Customer, Product

class CustomerForm(forms.ModelForm):
    first_name =forms.CharField(label='', required=True, widget=forms.TextInput(attrs={ "placeholder":"Imię *", "class":"input_field"}))
    last_name  =forms.CharField(label='', required=True, widget=forms.TextInput(attrs={ "placeholder":"Nazwisko *", "class":"input_field"}))
    phone      =forms.CharField(label='', required=True, widget=forms.NumberInput(attrs={ "placeholder":"Numer telefonu *", "class":"input_field"}))
    email      =forms.EmailField(label='', required=False, widget=forms.EmailInput(attrs={ "placeholder":"Adres e-mail", "class":"input_field"}))

    
    class Meta:
        model = Customer
        fields = [
            'first_name',
            'last_name',
            'phone',
            'email',
        ]   
    

    def clean_email(self):
        # Get the email
        email = self.cleaned_data.get('email')
        if email == "" :
            return None

        # Check to see if any users already exist with this email as a username.
        try:
            match = Customer.objects.get(email=email)
        except Customer.DoesNotExist:
            # Unable to find a user, this is fine
            return email

        # A user was found with this as a username, raise an error.
        raise forms.ValidationError('Wprowadzony e-mail już istnieje.')


class ProductForm(forms.ModelForm):
    first_name =forms.CharField(label='', required=True, widget=forms.TextInput(attrs={ "placeholder":"Imię *", "class":"input_field"}))
    last_name  =forms.CharField(label='', required=True, widget=forms.TextInput(attrs={ "placeholder":"Nazwisko *", "class":"input_field"}))
    phone      =forms.CharField(label='', required=True, widget=forms.NumberInput(attrs={ "placeholder":"Numer telefonu *", "class":"input_field"}))
    email      =forms.EmailField(label='', required=False, widget=forms.EmailInput(attrs={ "placeholder":"Adres e-mail", "class":"input_field"}))

    
    class Meta:
        model = Product
        fields = [
            'name',
            'quantity',
            'threshold',
        ]   
    

    def clean_email(self):
        # Get the email
        name = self.cleaned_data.get('name')
        # Check to see if any users already exist with this email as a username.
        try:
            match = Product.objects.get(email=name)
        except Product.DoesNotExist:
            # Unable to find a user, this is fine
            return name

        # A user was found with this as a username, raise an error.
        raise forms.ValidationError('Wprowadzony produkt już istnieje.')