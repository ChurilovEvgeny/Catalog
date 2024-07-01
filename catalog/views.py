from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from catalog.models import Product, Contact, Blog


# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         print(f"name={name}\nphone={phone}\nmessage={message}")
#
#     contacts = Contact.objects.all().values()
#     template = loader.get_template('catalog/contacts.html')
#     context = {
#         'contacts': contacts,
#     }
#     return HttpResponse(template.render(context, request))

class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'preview', 'category', 'price_per_purchase')
    success_url = reverse_lazy('catalog:product_list')


class ProductListView(ListView):
    model = Product
    paginate_by = 4


class ProductDetailView(DetailView):
    model = Product


class ContactListView(ListView):
    model = Contact


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'body', 'preview', 'is_published', 'views_count')
    success_url = reverse_lazy('catalog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)


class BlogListView(ListView):
    model = Blog
    paginate_by = 4

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'slug', 'body', 'preview', 'is_published', 'views_count')

    # success_url = reverse_lazy('catalog:blog_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object

    def get_success_url(self):
        return reverse('catalog:blog_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blog_list')


def blog_toggle_is_published(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.is_published = not blog.is_published
    blog.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
