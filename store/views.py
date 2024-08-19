
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from store.models import Product

def index(request):
    products = Product.objects.all()  # Assurez-vous que l'indentation est correcte
    context = {'products': products}
    return render(request, 'store/index.html', context)  # Veillez à ce que cette ligne soit également correctement indentée

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return HttpResponse(f"Product name: {product.name}")
