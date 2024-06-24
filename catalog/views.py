from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader

from catalog.models import Product, Contact


# Create your views here.

def home(request):
    products = Product.objects.all()
    template = loader.get_template('home.html')
    context = {
        'products': products
    }
    return HttpResponse(template.render(context, request))


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


def product(request, pk):
    prod = get_object_or_404(Product, pk=pk)
    template = loader.get_template('product.html')
    context = {
        'prod': prod
    }
    return HttpResponse(template.render(context, request))
