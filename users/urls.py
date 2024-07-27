from django.urls import path

from catalog.views import ContactPageView, ProductCreateView, ProductListView, ProductDetailView, ProductUpdateView
from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('contacts/', ContactPageView.as_view(), name='contact_view'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
]
