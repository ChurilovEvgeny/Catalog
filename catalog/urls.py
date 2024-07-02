from django.urls import path

from catalog.views import ContactPageView, ProductCreateView, ProductListView, ProductDetailView

from catalog.apps import CatalogConfig
app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('contacts/', ContactPageView.as_view(), name='contact_view'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
]
