from django.db import transaction
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import DetailView, ListView, CreateView, TemplateView, UpdateView

from catalog.forms import ProductForm, ProductVersionForm
from catalog.models import Product, Contact, ProductVersion


class VersionMixin():
    """Mixin class для создания formset версии продукта для продукта.
        Примешивать в левой позиции"""

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormSet = inlineformset_factory(self.model, ProductVersion, form=ProductVersionForm, extra=1)
        if self.request.method == 'POST':
            version_form_set = VersionFormSet(self.request.POST, instance=self.object)
        else:
            version_form_set = VersionFormSet(instance=self.object)
        context_data['formset'] = version_form_set
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        version_form_set = context_data['formset']
        with transaction.atomic():
            if form.is_valid() and version_form_set.is_valid():
                self.object = form.save()
                version_form_set.instance = self.object
                version_form_set.save()

        return super().form_valid(form)


class ProductCreateView(VersionMixin, CreateView):
    model = Product
    # success_url = reverse_lazy('catalog:product_list')
    form_class = ProductForm

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])


class ProductListView(ListView):
    model = Product
    paginate_by = 4


class ProductDetailView(DetailView):
    model = Product


class ProductUpdateView(VersionMixin, UpdateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])


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
