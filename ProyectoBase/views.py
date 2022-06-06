from django.http import HttpResponse
from django.shortcuts import render

def index_view(request):
    return render(request, 'index.html',context={})

def paquete_view(request):
    return render(request, 'index1.html',context={})

def oferta_view(request):
    return render(request, 'index2.html',context={})

def cliente_view(request):
    return render(request, 'index3.html',context={})

def contacto_view(request):
    return render(request, 'index4.html',context={})

def facebook_view(request):
    return render(request, 'facebook.html',context={})

def twitter_view(request):
    return render(request, 'twitter.html',context={})
    