import pathlib
import uuid

from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView

from catalog.models import Product, Contact
from config.settings import MEDIA_ROOT


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"name={name}\nphone={phone}\nmessage={message}")

    contacts = Contact.objects.all().values()
    template = loader.get_template('contacts.html')
    context = {
        'contacts': contacts,
    }
    return HttpResponse(template.render(context, request))


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'preview', 'category', 'price_per_purchase')
    success_url = reverse_lazy('catalog:product_list')


class ProductListView(ListView):
    model = Product
    paginate_by = 4


class ProductDetailView(DetailView):
    model = Product
