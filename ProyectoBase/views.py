from django.http import HttpResponse
from django.shortcuts import render
from costumer.models import Cliente


def index_view(request):
    return render(request, 'index.html',context={})

def paquete_view(request):
    return render(request, 'index-1.html',context={})

def oferta_view(request):
    return render(request, 'index-2.html',context={})

def persona_view(request):
    return render(request, 'index-3.html',context={})
    
def cliente_view(request):
    clientes = Cliente.objects.all()
    context = {'clientes': clientes}
    return render(request, "index-3.html", context = context) 

def contacto_view(request):
    return render(request, 'index-4.html',context={})

def facebook_view(request):
    return render(request, 'facebook.html',context={})

def twitter_view(request):
    return render(request, 'twitter.html',context={})
    