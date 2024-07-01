from django.urls import path

from catalog.views import ContactListView, ProductCreateView, ProductListView, ProductDetailView, BlogListView, \
    BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView, blog_toggle_is_published

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('contacts/', ContactListView.as_view(), name='contact_view'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product_detail'),

    path('blog_form/', BlogCreateView.as_view(), name='blog_create'),
    path('blog_list/', BlogListView.as_view(), name='blog_list'),
    path('blog_detail/<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
    path('blog_form/<int:pk>', BlogUpdateView.as_view(), name='blog_update'),
    path('blog_delete/<int:pk>', BlogDeleteView.as_view(), name='blog_delete'),
    path('blog_toggle_is_published/<int:pk>', blog_toggle_is_published, name='blog_toggle_is_published')
]