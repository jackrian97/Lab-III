# Curso de laboratorio de softare III
En este curso exploraremos la creacion de una plicacion web usando el framework Django, desde un sistema operativo linux intalado en una maquina virtual en google cloud, el motor de base de datos sera PostgresSQL para realizar el CRUD y por ultimo atulizaremos la plataforma de fl0 para desplegar esa base de datos.

# Índice

- [Proyecto ejemplo(arepas)](#arepas)
- [Ambiente virtual](#instalar-el-ambiente-virtual)
- [Django y app](#instalar-el-framework-django)
- [Base de datos](#conectar-base-de-datos-con-django)


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
Primero instalamos el paquete de psycopg2 con el comando
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
Y por ultimo creamos la tabla en la bese de datos ejecutando el comando
```bash
python manage.py migrate
```
