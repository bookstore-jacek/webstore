"""bookstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from pages.views import home_view, worker_view, contact_view, update_db_view
from ExtOrder.views import find_order_view, check_status_view, add_order_view
from Product.views import raport_view, update_prod_view, add_product_view, html_to_pdf_view, find_book_view, staff_find_book_view
from OrderedProduct.views import stock_update_view
from Customer.views import customers_view, personal_orders_view, add_customer_view

from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home_view, name='home'),
    path('kontakt/', contact_view, name='contact'),
    path('zamowienia/', personal_orders_view, name='personal_orders'),
    path('znajdz-ksiazke/', find_book_view, name='find_book'),
    path('sprawdz-status/', check_status_view, name='check_status'),

    path('panel/', worker_view, name='panel'),
    path('panel/raport/', raport_view, name='raport'),
    path('panel/klienci/', customers_view, name='customers'),
    path('panel/zamowienia/', find_order_view, name='find_order'),
    path('panel/asortyment/', update_db_view, name='update_db'),
    path('panel/dodaj-klienta/', add_customer_view, name='add_customer'),
    path('panel/dodaj-produkt/', add_product_view, name='add_product'),
    path('panel/lista-produktow/', staff_find_book_view, name='staff_find_book'),
    path('panel/dodaj-zamowienie/', add_order_view, name='add_order'),
    path('panel/aktualizuj-produkt/', update_prod_view, name='update_prod'),
    path('panel/zamowienie-hurtowe/', html_to_pdf_view, name='generate_pdf'),
    path('panel/zaktualizuj-asortyment/', stock_update_view, name='stock_update'),

    #dynamic links:
    path('zamowienie/', include('ExtOrder.urls')),
    path('produkt/', include('Product.urls'))
]