from http.client import HTTPResponse
from django.shortcuts import render
from costumer.models import Cliente
from costumer.forms import costumer_form
from django.http import HttpResponse

def create_customer_view(request):
    if request.method == 'GET':
        form = costumer_form()
        context = {'form' :form}
        return render(request, 'carga_customer.html', context = context)
    else:
        form = costumer_form(request.POST)
        if form.is_valid():
            new_customer = Cliente.objects.create(
                nombre = form.cleaned_data['nombre'],
                apellido = form.cleaned_data['apellido'],
                pasaporte = form.cleaned_data['pasaporte'],
                vencimiento = form.cleaned_data['vencimiento'], 
                dni = form.cleaned_data['dni'],
                domicilio = form.cleaned_data['domicilio'], 
                telefono = form.cleaned_data['telefono']
            )
            context = {'new_customer' : new_customer}
        return render(request, 'carga_customer.html', context = context)