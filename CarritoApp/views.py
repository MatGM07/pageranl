from django.shortcuts import render, HttpResponse, redirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from CarritoApp.Carrito import Carrito
from CarritoApp.models import Producto
from django.contrib.auth.decorators import login_required

@login_required
def tienda(request):
    username = request.user.username if request.user.is_authenticated else None
    #return HttpResponse("Hola Pythonizando")
    productos = Producto.objects.all()
    return render(request, "tienda.html", {'productos':productos,'username':username})
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
def ver_producto(request, producto_id):
    # Obtener el producto por su id
    producto = get_object_or_404(Producto, id=producto_id)
    # Renderizar la plantilla con los detalles del producto
    return render(request, 'detalle_producto.html', {'producto': producto})