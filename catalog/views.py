from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError, PermissionDenied
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, TemplateView, UpdateView, DeleteView

from catalog.forms import ProductForm, ProductVersionForm, ProductModeratorForm
from catalog.models import Product, Contact, ProductVersion


class VersionMixin:
    """Mixin class для создания formset версии продукта для продукта.
        Примешивать в левой позиции"""

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormSet = inlineformset_factory(self.model, ProductVersion, form=ProductVersionForm, extra=1)
        if self.request.method == 'POST':
            version_form_set = VersionFormSet(self.request.POST, instance=self.object)
        else:
            version_form_set = VersionFormSet(instance=self.object)

        if 'formset' not in context_data:
            context_data['formset'] = version_form_set

        return context_data

    def form_valid(self, form):
        version_form_set = self.get_context_data()['formset']
        self.object = form.save()
        if version_form_set.is_valid():
            # Мне не нравится, но это способ рабочий
            # Почему-то через queryset, filter, count не работало
            # count = sum([1 for item in version_form_set.get_queryset() if item.is_active])
            # При добавлении новой группы (элемента) в formset правильнее оказалось использование cleaned_data
            count = sum([1 for item in version_form_set.cleaned_data if item.get('is_active')])
            if count > 1:
                for fs_form in version_form_set.forms:
                    if fs_form.instance.is_active:
                        fs_form.add_error("is_active",
                                          ValidationError("Одновременно может быть выбрана только одна версия"))

                return self.form_invalid(form, version_form_set)

            version_form_set.instance = self.object
            version_form_set.save()

        return super().form_valid(form)

    def form_invalid(self, form, version_form_set=None):
        context = self.get_context_data()
        context['form'] = form
        # данная проверка и version_form_set=None нужны, чтобы правильно отрабатывало при ошибке основной формы
        if version_form_set is not None:
            context['formset'] = version_form_set
        return self.render_to_response(context)


class ProductCreateView(LoginRequiredMixin, VersionMixin, CreateView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')
    login_url = reverse_lazy('users:login')
    form_class = ProductForm

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductListView(ListView):
    model = Product
    paginate_by = 4


class ProductDetailView(DetailView):
    model = Product


class ProductUpdateView(LoginRequiredMixin, VersionMixin, UpdateView):
    model = Product
    form_class = ProductForm
    login_url = reverse_lazy('users:login')

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])

    def get_form_class(self):
        user = self.request.user
        if user.is_superuser or user == self.object.owner:
            return ProductForm
        elif user.has_perm("catalog.change_is_published") and user.has_perm(
                "catalog.change_description") and user.has_perm("catalog.change_category"):
            return ProductModeratorForm

        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')
    login_url = reverse_lazy('users:login')


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
