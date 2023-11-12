# En tu archivo reproductor/views.py
from django.shortcuts import render,redirect
from .models import Cancion
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required
def lista_canciones(request):
    canciones = Cancion.objects.all()
    return render(request, 'pages/musica.html', {'canciones': canciones})
def exit(request):
    logout(request)
    return redirect('inicio')
