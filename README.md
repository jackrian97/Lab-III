# Curso de laboratorio de softare III
En este curso exploraremos la creacion de una plicacion web usando el framework Django, desde un sistema operativo linux intalado en una maquina virtual en google cloud, el motor de base de datos sera PostgresSQL para realizar el CRUD y por ultimo atulizaremos la plataforma de fl0 para desplegar esa base de datos.
# Índice
- [Proyecto ejemplo(arepas)](#arepas)
- [Ambiente virtual](#instalar-el-ambiente-virtual)
- [Django y app](#instalar-el-framework-django)
- [Base de datos](#conectar-base-de-datos-con-django)
- [Vistas genericas(CRUD)](#vistas-genericascrud)
- [Vistas HTML con Bootstrap](#vistas-html-con-bootstrap)
- [Templates HTML](#templates-html)

# arepas
Vamos ha realizar la guia del profesor paso a paso https://github.com/cgiohidalgo/cruddjango20241 

## Instalar el ambiente virtual
Si no se tiene tiene el paquete de virtualenv se descarga con el siguiente comando en terminal
```bash
pip3 install virtualenv
```
Despues vamos a el directorio raiz del proyecto que en este caso se llamar arepas y creo la carpeta arepas_env con el comando
```bash
python3 -m venv arepas_env
```
Por ultimo para activar el ambiente virtual ejecutamos el comando
```bash
source arepas_env/bin/activate
```
Asegurate de estar en en la carpeta raiz arepas!!!
## instalar el framework Django
Para instalar Django ejecutamos el comando
```bash
pip3 install django
```
Ahora creamos un proyecto nuevo con el comando 
```bash
django-admin startproject arepas_proyecto
```
Asegurate de estar en en la carpeta raiz arepas!!! ya que arepas_proyecto debe estar al mismo nivel de arepas_env

Continuamos con la creacion de una app en Django, para ello nos vamos a mover a arepas_proyecto y ejecutamos el siguiente comando
```bash
python manage.py startapp arepas_app
```
Seguimos con el registro de la app modificando el fichero setting.py que esta ubicado en `/arepas/arepas_proyecto/arepas_proyecto/settings.py`
```python
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'arepas_app', #agrego la app
]
```
## Conectar base de datos con Django
Primero instalamos el paquete de psycopg2 con el comando, este paquete se utiliza para conectar Django con la base de datos PostgreSQL.
```bash
pip3 install psycopg2-binary==2.9.5
```
Seguimos con la configuracion de la base de datos en el fichero setting.py que esta ubicado en `/arepas/arepas_proyecto/arepas_proyecto/settings.py`
```python
DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.postgresql_psycopg2', #motor de base de datos
        'NAME' : 'lab1', #nombre de la base de datos
        'USER' : 'fl0user', #usuario de la base de datos
        'PASSWORD' : 'gEr0M9WAvKZF', #contraseña de la base de datos
        'HOST' : 'ep-cool-band-a5o631yc.us-east-2.aws.neon.fl0.io', #host de la base de datos
        'PORT' : '5432', #si lo dejas vacío tomara el puerto por default
    }
}
```
En este caso la base de datos esta en un servidor de fl0, si la base de datos esta en tu maquina local solo debes cambiar el host por localhost y el puerto por el que tengas configurado.

Seguimos con la creacion del modelo en la app, para ello modificamos el fichero `models.py` que esta ubicado en `/arepas/arepas_proyecto/arepas_app/models.py`
```python
from django.db import models

# Create your models here.
class Arepa(models.Model):  #nombre de la tabla en la Base de Datos
    nombre = models.CharField(max_length=100, default='DEFAULT VALUE')
    precio = models.CharField(max_length=20, default='DEFAULT VALUE')
    stock = models.CharField(max_length=100, default='DEFAULT VALUE')
    img = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
     db_table = 'arepas' #nombre de instancia con la que llamamos la tabla en la Base de Datos
```
Seguimos con la migracion de los modelos a la base de datos con el comando, asegurate de estar en `arepas_proyecto`
```bash
python manage.py makemigrations arepas_app
```
`makemigrations` Crea archivos de migración basados en los cambios en los modelos

Y por ultimo creamos la tabla en la bese de datos ejecutando el comando
```bash
python manage.py migrate
```
`migrate`  Aplica esas migraciones para crear o actualizar la estructura de la base de datos.
## Vistas genericas(CRUD)
Django proporciona vistas genéricas que facilitan la implementación de operaciones CRUD (Crear, Leer, Actualizar y Eliminar) en una aplicación web, estas vistas genéricas son:
- ListView: Muestra una lista de objetos.
- DetailView: Muestra los detalles de un objeto.
- CreateView: Crea un nuevo objeto.
- UpdateView: Actualiza un objeto existente.
- DeleteView: Elimina un objeto existente.

Para ello modificamos el fichero `views.py` que esta ubicado en `/arepas/arepas_proyecto/arepas_app/views.py`
```python
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
```
Seguimos con la creacion de las vistas en el mismo fichero `views.py`
```python
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
```
Finalmente definimos las URLS para dirigir las solicitudes HTTP entrantes a las vistas correspondientes en el fichero `urls.py` que esta ubicado en `/arepas/arepas_proyecto/arepas_proyecto/urls.py`
```python
from django.contrib import admin
from django.urls import path
from  arepas_app.views import ArepaListado, ArepaDetalle, ArepaCrear, ArepaActualizar, ArepaEliminar

urlpatterns = [
    #Define la ruta para acceder a la interfaz de administración de Django.
    path('admin/', admin.site.urls),
    #Define la ruta para mostrar la lista de "arepas". Cuando se accede a arepas/, se llama a la vista ArepaListado y se renderiza el template index.html.
    path('arepas/', ArepaListado.as_view(template_name = "arepas/index.html"), name='leer'),
    #Define la ruta para mostrar los detalles de una "arepa". Cuando se accede a arepas/detalle/<int:pk>, se llama a la vista ArepaDetalle y se renderiza el template detalles.html.
    path('arepas/detalle/<int:pk>', ArepaDetalle.as_view(template_name = "arepas/detalles.html"), name='detalles'),
    #Define la ruta para crear una nueva "arepa". Cuando se accede a arepas/crear, se llama a la vista ArepaCrear y se renderiza el template crear.html.
    path('arepas/crear', ArepaCrear.as_view(template_name = "arepas/crear.html"), name='crear'),
    #Define la ruta para actualizar una "arepa". Cuando se accede a arepas/editar/<int:pk>, se llama a la vista ArepaActualizar y se renderiza el template actualizar.html.
    path('arepas/editar/<int:pk>', ArepaActualizar.as_view(template_name = "arepas/actualizar.html"), name='actualizar'),
    #Define la ruta para eliminar una "arepa". Cuando se accede a arepas/eliminar/<int:pk>, se llama a la vista ArepaEliminar.
    path('arepas/eliminar/<int:pk>', ArepaEliminar.as_view(), name='eliminar'),
]
```
## Vistas HTML con Bootstrap
Primero crear la carpeta `templates` en `/arepas/arepas_proyecto/arepas_app/` y dentro de esta carpeta crear otra carpeta llamada `arepas` y dentro de esta carpeta crear los siguientes archivos:
- `index.html`
- `detalles.html`
- `crear.html`
- `actualizar.html`

Continuamos con la instalacion de Bootstrap 4 para Django, para ello vamos a instalar el paquete de django-bootstrap4 con el comando
```bash
pip install django-bootstrap4
```
El framework Bootstrap 4 se utiliza para diseñar y personalizar la interfaz de usuario de nuestra aplicación web.
Ahora seguimos con Widget Tweaks para Django, para ello vamos a instalar el paquete de django-widget-tweaks con el comando
```bash
pip install django-widget-tweaks
```
Widget Tweaks es una biblioteca de Django que permite personalizar los widgets de formularios de Django en las plantillas HTML.
Por ultimo modificamos el fichero `settings.py` que esta ubicado en `/arepas/arepas_proyecto/arepas_proyecto/settings.py` en la seccion de `INSTALLED_APPS` agregamos `'bootstrap4', 'widget_tweaks'`
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'arepas_app', #agrego la app
    'bootstrap4', #agrego bootstrap
    'widget_tweaks', #agrego widget_tweaks
]
```
En este mismo fichero `settings.py` en la seccion de `STATIC_URL = 'static/'` agregamos justo debajo el siguiente codigo
```python
#La URL para los archivos Estáticos (CSS, JS, Imágenes, etc.)
STATIC_URL = '/static/' 

#Las rutas para las imágenes de cada registro o arepas 
MEDIA_URL = '/arepas/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'arepas/static/uploads')

# Activamos 'CookieStorage' que nos permite enviar los mensajes de respuesta al Crear, Eliminar y Actualizar un registro
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'
```
## Templates HTML
Para empezar todos los archivos HTML deben tener la siguiente estructura
```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Tu título aquí</title>

  <!-- Cargamos la librería Bootstrap 4 -->
  {% load bootstrap4 %}

  <!-- CSS Bootstrap -->
  {% bootstrap_css %}

  <!-- Widget Tweaks -->
  {% load widget_tweaks %}

  <!-- Archivos estáticos -->
  {% load static %}

</head>
<body>

  <!-- Contenido segun la página -->

  <!-- Al final del body -->
  <!-- JS y jQuery de Bootstrap -->
  {% bootstrap_javascript jquery='full' %}

</body>
</html>
```
Empezamos con el archivo `index.html` el cual agragaremos en el body el siguiente codigo
```html
<body>
    <div align="left" class="btn_crear mb-3">
        <a href="crear" type="button" class="btn btn-primary">Crear</a> <!-- Boton crear -->
    </div>

    <table class="table table-striped table-hover">
        <thead>
            <tr>
                <th width="35%">Nombre</th>
                <th>Precio</th>
                <th>Stock</th>
                <th>Imagen</th>
                <th>Acciones</th>
            </tr>
        </thead>
        <tbody>
        <!-- Recorremos los objetos o registros que tenemos en nuestra tabla 'Arepas' y los listamos -->
        {% for arepas in object_list %}
        <tr>
            <td>{{ arepas.nombre }}</td>
            <td>{{ arepas.precio }}</td>
            <td>{{ arepas.stock }}</td>
            <td><img src="{% static 'uploads/'%}{{arepas.img}}" alt="{{arepas.nombre}}" class="img-fluid" width="7%"></td>
            <td>
                <!-- Usaremos un formulario que realizará la tarea de eliminar un registro o postre desde la misma tabla HTML -->
                <form method="POST" action="eliminar/{{arepas.id}}">
                    {% csrf_token %}
                    <div class="btn-group">
                        <!-- Creamos 3 botones que son ver, Editar y Eliminar, nos sirven para gestionar nuestros registros o postres -->
                        <a href="detalle/{{arepas.id}}" title="Ver" type="button" class="btn btn-success">Ver </a>
                        <a href="editar/{{arepas.id}}" title="Editar" type="button" class="btn btn-primary">Editar
                        </a>
                        <button class="btn btn-danger" onclick="return eliminar();" type="submit">Eliminar</button>
                    </div>
                </form>
            </td>
        </tr>
        {% endfor %}
        </tbody>
    </table>

    <!-- JS y jQuery de Bootstrap -->
    {% bootstrap_javascript jquery='full' %}

</body>
```
Continuamos con el archivo `crear.html` el cual agragaremos en el body el siguiente codigo
```html
<body>
  <form method="post" enctype="multipart/form-data">
    <!--Esta etiqueta asegura la protección contra CSRF (Cross-Site Request Forgery). Agrega un campo oculto con un token único que se utiliza para verificar que el formulario sea enviado desde tu sitio web y no desde un sitio malicioso.-->
    {% csrf_token %}
    <!--campo de la entrada de nombre de la 'arepa'-->
    <div class="form-group">
      <label for="nombre" class="txt_negrita">Nombre</label>
      <!-- Usamos la librería 'widget_tweaks' para crear esta caja de texto -->
      {{ form.nombre|add_class:"form-control" }}
    </div>
    <div class="form-group">
      <label for="precio" class="txt_negrita">Precio</label>
      {{ form.precio|add_class:"form-control" }}
  </form>
  <div class="form-group">
    <label for="stock" class="txt_negrita">Stock</label>
    {{ form.stock|add_class:"form-control" }}
  </div>
  <div class="form-group">
    <label for="img" class="txt_negrita">Imagen</label>
    {{ form.img|add_class:"form-control mb-3" }}
  </div>
  
  <!--Estos son los botones de enviar y cancelar-->
  <button type="submit" class="btn btn-primary">Aceptar</button>
  <a href="./"  type="submit" class="btn btn-primary">Cancelar</a>

  <!-- JS y jQuery de Bootstrap -->
  {% bootstrap_javascript jquery='full' %}
</body>
```
Continuamos con el archivo `detalles.html` el cual agragaremos en el body el siguiente codigo
```html
<body>
    <h1>Detalles</h1>
    <!-- Mostramos los detalles de una arepa en específico -->
    <p><span class="txt_negrita">Nombre:</span> <br> {{object.nombre}}</p>
    <p><span class="txt_negrita">Precio:</span> <br> {{object.precio}}</p>
    <p><span class="txt_negrita">Stock:</span> <br> {{object.stock}}</p>
    <p><span class="txt_negrita">Imagen:</span> <br> <img src="{% static 'uploads/'%}{{object.img}}" alt="{{object.nombre}}" class="img-fluid"> </p>
    <p><span class="txt_negrita">Creado:</span> <br> {{object.created_at}}</p>
    <p><span class="txt_negrita">Actualizado:</span> <br> {{object.updated_at}}</p>
    <!--Botón para ir Home-->
    <a href="../" type="submit" class="btn btn-primary">Volver</a> 
  <!-- JS y jQuery de Bootstrap -->
  {% bootstrap_javascript jquery='full' %}

</body>
```
Por ultimo el archivo `actualizar.html` el cual agragaremos en el body el siguiente codigo
```html
<body>
    <form method="post" enctype="multipart/form-data">
        {% csrf_token %}   
        <div class="form-group">
        <label for="nombre" class="txt_negrita">Nombre</label>
        {{ form.nombre|add_class:"form-control" }} <!-- Usamos la librería 'widget_tweaks' para crear esta caja de texto -->
        </div>
        <div class="form-group">
        <label for="precio" class="txt_negrita">Precio</label>
        {{ form.precio|add_class:"form-control" }}
        </div>
        <div class="form-group">
        <label for="stock" class="txt_negrita">Stock</label>
        {{ form.stock|add_class:"form-control" }}
        </div>
        <div class="form-group">
        <label for="img" class="txt_negrita">Imagen</label>
        {{ form.img|add_class:"form-control mb-3" }}
        <p class="txt_negrita">Imagen Actual:</p>
        <img src="{% static 'uploads/'%}{{object.img}}" class="img-fluid" alt="{{object.nombre}}">
        </div>

        <button type="submit" class="btn btn-primary">Aceptar</button>
        <a href="../" type="submit" class="btn btn-primary">Volver</a>
    </form> 
  <!-- JS y jQuery de Bootstrap -->
  {% bootstrap_javascript jquery='full' %}
</body>
```
