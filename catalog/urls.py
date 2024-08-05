from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.views import ContactPageView, ProductCreateView, ProductListView, ProductDetailView, ProductUpdateView, \
    ProductDeleteView, CategoryListView

from catalog.apps import CatalogConfig
app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('contacts/', ContactPageView.as_view(), name='contact_view'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('product_delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),

    path('categories/', CategoryListView.as_view(), name='category_list')
]
