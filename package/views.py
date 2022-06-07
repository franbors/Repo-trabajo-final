from django.shortcuts import render
from package.forms import Paquete_form
from package.models import Paquete


""" def list_paquetes(request):
    paquetes = Paquete.objects.all()
    context = {'paquetes':paquetess}
    return render(request, 'products.html', context=context) """

def create_paquetes(request):
    if request.method == 'GET':

        form = Paquete_form()
        context = {'form':form}

        return render(request, 'create_paquetes.html', context=context)

    elif request.method == 'POST':
        
        form = Paquete_form(request.POST)
        if form.is_valid():
            new_paquete = Paquete.objects.create(
                destino = form.cleaned_data['destino'],
                descripcion = form.cleaned_data['descripcion'],
                dias = form.cleaned_data['dias'],
                fecha_partida = form.cleaned_data['fecha_partida'],
                fecha_regreso = form.cleaned_data['fecha_regreso'],
                precio_publico = form.cleaned_data['precio_publico'],
                costo = form.cleaned_data['costo'],
                oferta = form.cleaned_data['oferta'],
                Image_Set_1 = form.cleaned_data['Image_Set_1'],
                Image_Set_2 = form.cleaned_data['Image_Set_2'],
                activo = form.cleaned_data['activo'],
            )
            context = {'new_paquete':new_paquete}
        else:
            context = {'errors':form.errors}
        return render(request, 'create_paquetes.html', context = context)

    else:
        return HttpResponse('Only GET and POST methods are allowed')
