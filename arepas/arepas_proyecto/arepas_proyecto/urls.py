"""
URL configuration for arepas_proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
