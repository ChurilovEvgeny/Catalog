from django.urls import path
from django.views.decorators.cache import never_cache

from blog.views import BlogListView, BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView, blog_toggle_is_published

from blog.apps import BlogConfig
app_name = BlogConfig.name

urlpatterns = [
    path('blog_form/', never_cache(BlogCreateView.as_view()), name='blog_create'),
    path('blog_list/', BlogListView.as_view(), name='blog_list'),
    path('blog_detail/<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
    path('blog_form/<int:pk>', never_cache(BlogUpdateView.as_view()), name='blog_update'),
    path('blog_delete/<int:pk>', BlogDeleteView.as_view(), name='blog_delete'),
    path('blog_toggle_is_published/<int:pk>', blog_toggle_is_published, name='blog_toggle_is_published')
]