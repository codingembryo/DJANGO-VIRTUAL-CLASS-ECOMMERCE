from django.urls import path, re_path
from ecommerce.productapp import views as product_view



urlpatterns = [
    re_path(r'^upload_product/', product_view.uploadProduct, name='upload_product'),
    re_path(r'^display_product/', product_view.displayProduct, name='display_product'),
]