from django.urls import path
from . import views
from .views import guardarCompra, saveCompra, saveProyecto, listarLider, eliminarCompra


urlpatterns = [
    path("", views.home),
    path("listarCompra/", views.listarCompra, name = "listaC"),
    path("guardarCompra/", views.guardarCompra, name = "saveC"),
    path("saveCompra/", views.saveCompra, name = "guardarC"),
    path("eliminacionCompra/<codigo>/", views.eliminarCompra, name = "deleteC"),
    path("editarCompra/<codigo>", views.editarCompra, name = "editC"),
    path("editarCompra/", views.edicionCompra, name = "editarC"),
    path("listProyectos/", views.listProyectos, name = "listaP"),
    path("saveProyecto/", views.saveProyecto, name = "guardarP"),
    path("guardarProyecto/", views.guardarProyecto, name = "guardarPro"),
    path("eliminarProyecto/<codigo>", views.eliminarProyecto, name = "deleteP"),
    path("edicionProyecto/<codigo>", views.edicionProyecto, name = "editarP"),
    path("editarProyecto", views.editarProyecto, name = "editP"),
    path("listarLider/", views.listarLider, name = "listaL"),
    path("eliminarLider/<codigo>", views.eliminarLider, name = "deleteL"),
    path("saveLider/", views.saveLider, name = "saveL"),
    path("guardarLider/", views.guardarLider, name = "liderG"),
    path("editLider/<codigo>", views.editLider, name = "editarL"),
    path("editarLider/", views.editarLider, name = "editL"),
    path("listTipo/", views.listTipo, name = "listT"),
    path("saveTipo/", views.saveTipo, name = "tipoG"),
    path("guardarTipo", views.guardarTipo, name = "saveG"),
    path("eliminarTipo/<codigo>", views.eliminarTipo, name = "deleteT"),
    path("editTipo/<codigo>", views.editTipo, name = "editT"),
    path("editarTipo/", views.editarTipo, name = "editarT"),
    path("listarMaterial/", views.listMaterial, name = "listaM"),
    path("saveMaterial/", views.saveMaterial, name = "saveM"),
    path("guardarMaterial/", views.guardarMaterial, name = "guardarM"),
    path("editMateriales/<codigo>", views.editMateriales, name = "editM"),
    path("editarMateriales/", views.editarMateriales, name = "editarM"),
    path("eliminarMaterial/<codigo>", views.eliminarMaterial, name = "eliminarM"),
]
