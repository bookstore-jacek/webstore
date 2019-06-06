
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

# from django.conf.urls import url

# from qr_code import views


# app_name = 'qr_code'
# urlpatterns = [
#     url(r'^images/serve_qr_code_image/$', qr_code.views.serve_qr_code_image, name='serve_qr_code_image')
# ]