from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('/shop', views.ProductForm, name='ProductForm'),
    # Add other URL patterns here
]