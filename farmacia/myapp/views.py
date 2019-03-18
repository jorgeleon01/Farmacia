from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from myapp.models import Producto

# Create your views here.

def index(request):
    producto_list = Producto.objects.all()
    paginator = Paginator(producto_list, 3)

    page = request.GET.get('page')
    productos = paginator.get_page(page)
    return render(request,'myapp/index.html',{'productos': productos})
