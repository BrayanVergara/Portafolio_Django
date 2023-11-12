# reproductor/urls.py
from django.urls import path
from .views import lista_canciones

app_name = 'reproductor' 

urlpatterns = [
    path('lista/', lista_canciones, name='lista_canciones'),

]
