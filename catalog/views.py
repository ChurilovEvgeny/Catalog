from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView, CreateView, TemplateView

from catalog.forms import ProductForm
from catalog.models import Product, Contact


class ProductCreateView(CreateView):
    model = Product
    # fields = ('name', 'description', 'preview', 'category', 'price_per_purchase')
    success_url = reverse_lazy('catalog:product_list')
    form_class = ProductForm


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
