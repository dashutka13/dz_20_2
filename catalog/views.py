from django.shortcuts import render


def index(request):
    return render(request, 'catalog/index.html')


def product(request):
    return render(request, 'catalog/product.html')
