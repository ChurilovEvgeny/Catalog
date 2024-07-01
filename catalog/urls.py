from django.urls import path

from catalog.views import ContactListView, ProductCreateView, ProductListView, ProductDetailView

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('contacts/', ContactListView.as_view(), name='contact_view'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
]