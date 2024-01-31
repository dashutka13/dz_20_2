from django.shortcuts import render

from catalog.models import Product


def catalog(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'Каталог'
    }

    return render(request, 'catalog/catalog.html', context)


def home_page(request):
    return render(request, 'catalog/home_page.html')


def product(request, pk):
    pokemon = Product.objects.get(pk=pk)

    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'title': f'Посмотри как прерасен {pokemon.name}'
    }

    return render(request, 'catalog/product.html', context)

