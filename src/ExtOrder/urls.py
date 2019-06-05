from django.urls import path
from .views import (
    detail_view,
    edit_view,
)

app_name = 'zamowienie'
urlpatterns = [
    path('<int:id>/', detail_view, name='order-detail'),
    path('<int:id>/edytuj', edit_view, name='order-edit'),
]