from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm

# READ - Listar productos
def inicio(request):
    productos = Producto.objects.all()
    return render(request, 'vista.html', {'productos': productos})

# CREATE - Crear producto (guardado manual)
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            # 👇 GUARDADO MANUAL porque es forms.Form, no ModelForm
            Producto.objects.create(
                nombre=form.cleaned_data['nombre'],
                descripcion=form.cleaned_data['descripcion'],
                precio=form.cleaned_data['precio']
            )
            return redirect('inicio')
    else:
        form = ProductoForm()
    return render(request, 'crear.html', {'form': form, 'accion': 'Crear'})

# UPDATE - Editar producto (actualización manual)
def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            # 👇 ACTUALIZACIÓN MANUAL
            producto.nombre = form.cleaned_data['nombre']
            producto.descripcion = form.cleaned_data['descripcion']
            producto.precio = form.cleaned_data['precio']
            producto.save()
            return redirect('inicio')
    else:
        # 👇 Precargamos el formulario con los datos del producto
        form = ProductoForm(initial={
            'nombre': producto.nombre,
            'descripcion': producto.descripcion,
            'precio': producto.precio,
        })
    return render(request, 'crear.html', {'form': form, 'accion': 'Editar'})

# DELETE - Eliminar producto
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('inicio')
    return render(request, 'confirmar_eliminar.html', {'producto': producto})