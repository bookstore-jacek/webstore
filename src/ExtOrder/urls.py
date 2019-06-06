
from django.urls import path
from .views import detail_view

app_name = 'zamowienie'
urlpatterns = [
    path('/panel/<int:id>/', detail_view, name='order-detail'),
]