from django.shortcuts import render


def inicio(request):
    """Pantalla mínima para verificar que la aplicación está conectada."""
    return render(request, 'catalogo/inicio.html')
