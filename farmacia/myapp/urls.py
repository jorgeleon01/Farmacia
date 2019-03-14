#from django.conf.urls import url, include
#from farmacia.myapp.views import index
from django.urls import path

from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='index'),
]
