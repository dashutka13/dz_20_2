from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index, product


app_name = CatalogConfig.name


urlpatterns = [
    path('', index),
    path('product/', product)
]