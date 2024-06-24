import pathlib
import uuid

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template import loader

from catalog.models import Product, Contact, Category
from config.settings import MEDIA_ROOT


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


def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        formFile = request.POST.get('formFile')
        category_id = request.POST.get('category')
        price = request.POST.get('price')
        print(f"name={name}\ndescription={description}\nformFile={formFile}\ncategory={category_id}\nprice={price}")

        bin_file = request.FILES.get('formFile')
        # if 'fromFile' in request.FILES:
        #     fileName = handle_uploaded_file(request.FILES['formFile'])
        # else:
        #     fileName = handle_uploaded_file(None)
        fileName = handle_uploaded_file(bin_file)

        cat = None if int(category_id) == 0 else Category.objects.get(pk=category_id)
        Product.objects.create(
            name=name,
            description=description,
            preview=fileName,
            category=cat,
            price_per_purchase=price)

    categories = Category.objects.all()

    template = loader.get_template('add.html')
    context = {
        'categories': categories
    }
    return HttpResponse(template.render(context, request))


def handle_uploaded_file(f) -> str | None:
    """
    Функция для загрузки изображений на сервер
    :param f: файл для загрузки
    :return: Имя сохраненного файла для записи в БД
    """
    if f is not None:
        # Генерируем уникальное имя str(uuid.uuid4())
        filename = pathlib.Path('products') / (str(uuid.uuid4()) + pathlib.Path(f.name).suffix)
        print("FNAM: ", filename)
        path = MEDIA_ROOT / filename
        with open(path, "wb+") as destination:
            for chunk in f.chunks():
                destination.write(chunk)
            return str(filename)

    return None
