# Curso de laboratorio de softare III
En este curso exploraremos la creacion de una plicacion web usando el framework Django, desde un sistema operativo linux intalado en una maquina virtual en google cloud, el motor de base de datos sera PostgresSQL para realizar el CRUD y por ultimo atulizaremos la plataforma de fl0 para desplegar esa base de datos.

# Índice

- [Proyecto ejemplo(arepas)](#arepas)
- [Ambiente virtual](#instalar-el-ambiente-virtual)
- [Django y app](#instalar-el-framework-django)


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

