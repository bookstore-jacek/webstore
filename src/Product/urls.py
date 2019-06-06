
from django.urls import path
from .views import (
    edit_view,
)

app_name = 'produkt'
urlpatterns = [
    path('<int:id>/edytuj/', edit_view, name='product-edit'),
]