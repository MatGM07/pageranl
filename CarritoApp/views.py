from django.shortcuts import render, HttpResponse, redirect
from django.shortcuts import render, get_object_or_404
from PageRank.models import UserViewCount
# Create your views here.
from CarritoApp.Carrito import Carrito
from CarritoApp.models import Producto
from django.contrib.auth.decorators import login_required
from PageRank.views import product_transition_view, pagerank
from PageRank.models import Transition,ProductProb

@login_required
def tienda(request):
    username = request.user.username if request.user.is_authenticated else None
    #return HttpResponse("Hola Pythonizando")
    productos = Producto.objects.all()
    IDsorganizados = ProductProb.objects.all().order_by('-Prob').values_list('Product', flat=True)
    arreglo = []
    for i in range (len(IDsorganizados)):
        arreglo.append(Producto.objects.get(id=IDsorganizados[i]))
    organizados = arreglo
    return render(request, "tienda.html", {'productos':productos,'username':username,'organizados':organizados})


@login_required
def lista_productos(request):
    username = request.user.username if request.user.is_authenticated else None
    productos = Producto.objects.all()
    return render(request, "listaProductos.html", {'productos': productos, 'username': username})

@login_required
def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("Tienda")
@login_required
def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("Tienda")
@login_required
def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("Tienda")
@login_required
def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("Tienda")

@login_required()
def ver_producto(request, producto_id, origen_id):
    # Obtener el producto por su id
    todos = Producto.objects.all()
    user_view_count, created = UserViewCount.objects.get_or_create(user=request.user)
    user_view_count.view_count += 1
    user_view_count.save()
    if (user_view_count.view_count>0) and (user_view_count.view_count%2 == 0):
        probabilidades = pagerank(Transition)
        h = 0
        for producto in todos:
            prob = probabilidades[h]
            nuevaProb, created = ProductProb.objects.get_or_create(user=request.user, Product=producto)
            nuevaProb.Prob=prob
            nuevaProb.save()
            h=h+1

    IDsorganizados = ProductProb.objects.all().order_by('-Prob').values_list('Product', flat=True)
    arreglo = []
    for i in range(len(IDsorganizados)):
        if i!=producto_id:
            arreglo.append(Producto.objects.get(id=IDsorganizados[i]))
    organizados = arreglo

    producto = get_object_or_404(Producto, id=producto_id)
    if origen_id != "a":
        numerica = int(origen_id)
        origen = get_object_or_404(Producto, id=origen_id)
        product_transition_view(request, origen.id, producto.id)
    # Renderizar la plantilla con los detalles del producto
    return render(request, 'detalle_producto.html', {'producto': producto,'organizados':organizados})



