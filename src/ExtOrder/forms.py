from django import forms   
from .models import ExtOrder as Order

class CustomerForm(forms.Form):
    text = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={ "placeholder":"Wyszukaj klienta *", "class": "input_field"}))

    

# class OrderForm(forms.ModelForm):
#     CHOICES=[('select1','select 1'),
#             ('select2','select 2')]
#     paid = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    
#     class Meta:
#         model = Order
#         fields = [
#             'paid',
#         ]   
    
#     # def clean_customer(self, *args, **kwargs):
#     #     email= self.cleaned_data.get("email")
#     #     if None in email:
#     #         return None

#     def clean_email(self):
#         # Get the email
#         email = self.cleaned_data.get('email')
#         if email == "" :
#             return None

#         # Check to see if any users already exist with this email as a username.
#         try:
#             match = Customer.objects.get(email=email)
#         except Customer.DoesNotExist:
#             # Unable to find a user, this is fine
#             return email

#         # A user was found with this as a username, raise an error.
#         raise forms.ValidationError('Wprowadzony e-mail już istnieje.')