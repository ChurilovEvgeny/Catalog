from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView, TemplateView
from pytils.translit import slugify

from catalog.models import Product, Contact, Blog
from config.settings import EMAIL_HOST_USER


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'preview', 'category', 'price_per_purchase')
    success_url = reverse_lazy('catalog:product_list')


class ProductListView(ListView):
    model = Product
    paginate_by = 4


class ProductDetailView(DetailView):
    model = Product


class ContactPageView(TemplateView):
    template_name = "catalog/contact_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contacts"] = Contact.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"name={name}\nphone={phone}\nmessage={message}")
        return HttpResponseRedirect(reverse('catalog:contact_view'))


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

    @staticmethod
    def send_notification(title):
        send_mail(
            'Сообщение с сайта',
            f'Ваш блог {title} достиг 100 просмотров',
            EMAIL_HOST_USER,
            ["churilov.e.a@yandex.ru"],
            fail_silently=False,
        )

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1

        # Если количество просмотров достигло 100, то отправляем сообщение на почту
        if self.object.views_count == 100:
            self.send_notification(self.object.title)

        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'slug', 'body', 'preview', 'is_published', 'views_count')

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
