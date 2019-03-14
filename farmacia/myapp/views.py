from django.shortcuts import render
from django.http import HttpResponse

from myapp.models import Producto

# Create your views here.

def index(request):
	#return HttpResponse("index")
	return render(request,'myapp/index.html',{'productos': Producto.objects.all()})
