from django.urls import path

from catalog.views import home, contacts, product

app_name = 'catalog'

urlpatterns = [
    path('', home, name='catalog'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>', product, name='product'),
]