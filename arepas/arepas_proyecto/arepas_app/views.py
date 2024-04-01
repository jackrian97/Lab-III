from django.shortcuts import render
from .models import Arepa # importamos el modelo Arepa
# Importamos las vistas genéricas de Django donde Listview nos permite listar y DetailView nos permite ver los detalles de un registro
from django.views.generic import ListView, DetailView
# Importamos las vistas genéricas de Django donde CreateView nos permite crear un registro, UpdateView nos permite actualizar un registro y DeleteView nos permite eliminar un registro
from django.views.generic.edit import CreateView, UpdateView, DeleteView
 # Se importa la función reverse de Django, que se utiliza para obtener la URL inversa a partir de un nombre de vista. Esto es útil para redireccionar después de realizar una acción en una vista.
from django.urls import reverse
# Aquí se importa el módulo messages de Django, que se utiliza para mostrar mensajes al usuario. Esto puede ser útil para mostrar mensajes de éxito, error u otra información después de realizar ciertas acciones.
from django.contrib import messages 
# Se importa SuccessMessageMixin, que es una clase de Django utilizada para habilitar mensajes de éxito en las vistas basadas en clases. Esto permite mostrar mensajes después de que se realizan ciertas acciones en las vistas basadas en clases.
from django.contrib.messages.views import SuccessMessageMixin
# Finalmente, se importa el módulo forms de Django, que se utiliza para trabajar con formularios en Django. Esto puede ser útil cuando necesitas crear formularios personalizados para recopilar información del usuario en tu aplicación.
from django import forms 

# CRUD de Arepas

class ArepaListado(ListView):
    model = Arepa # Llamamos a la clase 'Arepa' que se encuentra en nuestro archivo 'models.py'

class ArepaCrear(SuccessMessageMixin, CreateView): 
    model = Arepa # Llamamos a la clase 'Arepa' que se encuentra en nuestro archivo 'models.py'
    form = Arepa # Definimos nuestro formulario con el nombre de la clase o modelo 'Arepa'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'arepas' de nuestra Base de Datos 
    success_message = 'Arepa Creada Correctamente!' # Mostramos este Mensaje luego de Crear una Arepa

    # Redireccionamos a la página principal luego de crear un registro o arepa
    def get_success_url(self):        
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

class ArepaDetalle(DetailView): 
    model = Arepa # Llamamos a la clase 'Arepa' que se encuentra en nuestro archivo 'models.py' 

class ArepaActualizar(SuccessMessageMixin, UpdateView): 
    model = Arepa # Llamamos a la clase 'Arepa' que se encuentra en nuestro archivo 'models.py' 
    form = Arepa # Definimos nuestro formulario con el nombre de la clase o modelo 'Arepa' 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'arepas' de nuestra Base de Datos 
    success_message = 'Arepa Actualizada Correctamente !' # Mostramos este Mensaje luego de Editar un Arepa 

    # Redireccionamos a la página principal luego de actualizar un registro o arepa
    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

class ArepaEliminar(SuccessMessageMixin, DeleteView): 
    model = Arepa 
    form = Arepa
    fields = "__all__"     

    # Redireccionamos a la página principal luego de eliminar un registro o arepa
    def get_success_url(self): 
        success_message = 'Arepa Eliminada Correctamente !' # Mostramos este Mensaje luego de Editar una Arepa 
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
