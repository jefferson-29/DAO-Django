
from ast import Delete
from django.shortcuts import render, redirect
from .models import Compra, Proyecto, Materialconstruccion, Tipo, Lider
from django.core.paginator import Paginator
from django.http import Http404, HttpResponse
from django.contrib import messages


def home(request):
    return render(request, "index.html")

# Inicio CRUD compra
def listarCompra(request):
    proyectosList = Compra.objects.get_queryset().order_by('id_compra')
    page = request.GET.get("page", 1)
    
    try:
        paginator = Paginator(proyectosList, 50)
        proyectosList = paginator.page(page)
    except:
        raise Http404

    data = {
        "entity" : proyectosList,
        "paginator" : paginator
    }
    return render(request, "listar/listarCompras.html", data)

def guardarCompra(request):    
    listaDB = { "proyecto" : Proyecto.objects.values("id_proyecto", "constructora").distinct(),
                    "material" : Materialconstruccion.objects.all()}
    return render(request, "save/saveCompra.html", listaDB)

def saveCompra(request):
    cantidad = request.POST.get("txtCantidad")
    proveedor = request.POST.get("txtProveedor")
    pagado = request.POST.get("pagado")
    fecha = request.POST.get("fechaCompra")
    proyecto_id = request.POST.get("construccion")
    proyecto = Proyecto.objects.get(id_proyecto = proyecto_id)
    materialconstruccion_id = request.POST.get("construccion")
    materialconstruccion = Materialconstruccion.objects.get(id_materialconstruccion = materialconstruccion_id)

    compra = Compra.objects.create(
        cantidad = cantidad, proveedor = proveedor, pagado = pagado,
        fecha = fecha, 
        id_proyecto = proyecto,
        id_materialconstruccion  = materialconstruccion)

    return redirect("listaC")

def eliminarCompra(request, codigo):    

    try:
        compra = Compra.objects.get(id_compra = codigo)
        compra.delete()
        messages.success(request, "¡Eliminado Correctamente!")
        return redirect("listaC")
    except:
        messages.success(request, "No se encontro el registro de compra")
        return redirect("listaC")    

def editarCompra(request, codigo):
    compra = Compra.objects.get(id_compra = codigo)
    comprar = Compra.objects.all()
    materiales = Materialconstruccion.objects.all()
    proyecto = Proyecto.objects.all()
    return render(request, "edit/editarCompra.html", {"compra" : compra, "material" : materiales,
    "proyecto" : proyecto, "comprar" : comprar})

def edicionCompra(request):
    codigo = request.POST.get("id")
    cantidad = request.POST.get("txtCantidad")
    proveedor = request.POST.get("txtProveedor")
    pagado = request.POST.get("pagado")
    fecha = request.POST.get("fechaCompra")
    proyecto_id = request.POST.get("construccion")
    proyecto = Proyecto.objects.get(id_proyecto = proyecto_id)
    materialconstruccion_id = request.POST.get("construccion")
    materialconstruccion = Materialconstruccion.objects.get(id_materialconstruccion = materialconstruccion_id)

    compra = Compra.objects.get(id_compra = codigo)
    compra.cantidad = cantidad
    compra.proveedor = proveedor 
    compra.pagado = pagado
    compra.fecha = fecha
    compra.id_proyecto = proyecto
    compra.id_materialconstruccion  = materialconstruccion
    compra.save()
    return redirect("listaC")

#fin CRUD compra

#inicio CRUD proyecto

def saveProyecto(request):
    lista = {
        "proyecto" : Proyecto.objects.values("ciudad").distinct().order_by('ciudad'),
        "tipo" : Tipo.objects.all(),
        "lider" : Lider.objects.all().order_by('nombre')
    }
    return render(request, "save/saveProyecto.html", lista)

def listProyectos(request):
    proyectosList = Proyecto.objects.get_queryset().order_by('id_proyecto')
    page = request.GET.get("page", 1)
    
    try:
        paginator = Paginator(proyectosList, 50)
        proyectosList = paginator.page(page)
    except:
        raise Http404

    data = {
        "entity" : proyectosList,
        "paginator" : paginator
    }
    return render(request, "listar/listarProyecto.html", data)

def guardarProyecto(request):
    fechaProyecto = request.POST.get("fechaProyecto")
    constructora = request.POST.get("constructora")
    numBanos = request.POST.get("numBanos")
    numHabitaciones = request.POST.get("numHabitaciones")
    banco  = request.POST.get("banco")
    numPorcentaje = request.POST.get("numPorcentaje")
    ciudad = request.POST.get("ciudad")
    clasificacion = request.POST.get("clasificacion")
    acabado = request.POST.get("acabado")
    txtSerial = request.POST.get("txtSerial")
    tipo_id = request.POST.get("tipo")
    tipo = Tipo.objects.get(id_tipo = tipo_id)
    lider_id = request.POST.get("lider")
    nombreLider = Lider.objects.get(id_lider = lider_id)

    proyecto = Proyecto.objects.create(
      fecha_inicio = fechaProyecto, 
      constructora = constructora, 
      numero_banos = numBanos,
      numero_habitaciones = numHabitaciones, 
      banco_vinculado = banco, 
      porcentaje_cuota_inicial = numPorcentaje,
      ciudad = ciudad, 
      clasificacion = clasificacion, 
      acabados = acabado, 
      serial = txtSerial,
      id_tipo = tipo,
      id_lider  = nombreLider)
    #return HttpResponse(id_tipo)
    return redirect("/listProyectos/")

def eliminarProyecto(request, codigo):
    proyecto = Proyecto.objects.get(id_proyecto = codigo)
    proyecto.delete()

    return redirect("/listProyectos/")

def edicionProyecto(request, codigo):
    proyecto = Proyecto.objects.get(id_proyecto = codigo)
    proyectos = Proyecto.objects.all()
    tipo = Tipo.objects.all()
    lider = Lider.objects.all()

    return render(request, "edit/editarProyecto.html", {"proyecto" : proyecto,
    "proyectos" : proyectos, 
    "proyec" : Proyecto.objects.values("ciudad").distinct().order_by('ciudad'),
    "tipo" : tipo,
    "lider" : lider})

def editarProyecto(request):
    codigo = request.POST.get("id")
    fechaProyecto = request.POST.get("fechaProyecto")
    constructora = request.POST.get("constructora")
    numBanos = request.POST.get("numBanos")
    numHabitaciones = request.POST.get("numHabitaciones")
    banco  = request.POST.get("banco")
    numPorcentaje = request.POST.get("numPorcentaje")
    ciudad = request.POST.get("ciudad")
    clasificacion = request.POST.get("clasificacion")
    acabado = request.POST.get("acabado")
    txtSerial = request.POST.get("txtSerial")
    tipo_id = request.POST.get("tipo")
    tipo = Tipo.objects.get(id_tipo = tipo_id)
    lider_id = request.POST.get("lider")
    nombreLider = Lider.objects.get(id_lider = lider_id)

    proyecto = Proyecto.objects.get(id_proyecto = codigo)
    proyecto.fecha_inicio = fechaProyecto
    proyecto.constructora = constructora
    proyecto.numero_banos = numBanos
    proyecto.numero_habitaciones = numHabitaciones
    proyecto.banco_vinculado = banco
    proyecto.porcentaje_cuota_inicial = numPorcentaje
    proyecto.ciudad = ciudad
    proyecto.clasificacion = clasificacion
    proyecto.acabados = acabado
    proyecto.serial = txtSerial
    proyecto.id_tipo = tipo
    proyecto.id_lider = nombreLider
    proyecto.save()

    return redirect("/listProyectos/")

#fin CRUD proyecto

#Inicio CRUD lider

def listarLider(request):
    liderList = Lider.objects.get_queryset().order_by('id_lider')
    page = request.GET.get("page", 1)
    
    try:
        paginator = Paginator(liderList, 50)
        liderList = paginator.page(page)
    except:
        raise Http404

    data = {
        "entity" : liderList,
        "paginator" : paginator
    }
    return render(request, "listar/listarLider.html", data)

def eliminarLider(request, codigo):
    lider = Lider.objects.get(id_lider = codigo)
    lider.delete()    

    return redirect("listaL")
    #return HttpResponse(id_tipo)

def saveLider(request):
    lista = {
        "ciudad" : Lider.objects.values("ciudad_residencia").distinct().order_by('ciudad_residencia')
    }
    return render(request, "save/saveLider.html", lista)

def guardarLider(request):
    nombre = request.POST.get("txtNombreL")
    primerApellido = request.POST.get("txtApellido")
    segundoApellido = request.POST.get("txtSapellido")
    salario = request.POST.get("salario")
    ciudadResidencia = request.POST.get("ciudad")
    cargo = request.POST.get("cargo")
    clasificacion = request.POST.get("clasificacion")
    documento = request.POST.get("txtId")
    fechaNacimiento = request.POST.get("fechaNacimiento")

    lider = Lider.objects.create(
        nombre = nombre,
        primer_apellido = primerApellido,
        segundo_apellido= segundoApellido,
        salario = salario,
        ciudad_residencia = ciudadResidencia,
        cargo = cargo,
        clasificacion = clasificacion,
        documento_identidad = documento,
        fecha_nacimiento = fechaNacimiento
    )

    return redirect("listaL")

def editLider(request, codigo):
    lider = Lider.objects.get(id_lider = codigo)
    lideres = Lider.objects.all()

    return render(request, "edit/editarLider.html", {"lider" : lider,
    "ciudad" : Lider.objects.values("ciudad_residencia").distinct().order_by('ciudad_residencia'),
    "lideres" : lideres})

def editarLider(request):
    codigo = request.POST.get("id")
    nombre = request.POST.get("txtNombreL")
    primerApellido = request.POST.get("txtApellido")
    segundoApellido = request.POST.get("txtSapellido")
    salario = request.POST.get("salario")
    ciudadResidencia = request.POST.get("ciudad")
    cargo = request.POST.get("cargo")
    clasificacion = request.POST.get("clasificacion")
    documento = request.POST.get("txtId")
    fechaNacimiento = request.POST.get("fechaLider")

    lider = Lider.objects.get(id_lider = codigo)
    lider.nombre = nombre
    lider.primer_apellido = primerApellido
    lider.segundo_apellido = segundoApellido
    lider.salario = salario
    lider.ciudad_residencia = ciudadResidencia
    lider.cargo = cargo
    lider.clasificacion = clasificacion
    lider.documento_identidad = documento
    lider.fecha_nacimiento = fechaNacimiento
    lider.save()

    return redirect("listaL")

#fin CRUD lider

#inicio CRUD Tipo

def listTipo(request):
    tipoList = Tipo.objects.get_queryset().order_by('id_tipo')
    page = request.GET.get("page", 1)
    
    try:
        paginator = Paginator(tipoList, 50)
        tipoList = paginator.page(page)
    except:
        raise Http404

    data = {
        "entity" : tipoList,
        "paginator" : paginator
    }
    return render(request, "listar/listarTipo.html", data)

def saveTipo(request):
    
    return render(request, "save/saveTipo.html")

def guardarTipo(request):
    codTipo = request.POST.get("codTipo")
    areaMax = request.POST.get("areaMax")
    financiable = request.POST.get("financiable")
    estrato = request.POST.get("estrato")

    tipo = Tipo.objects.create(
        codigo_tipo = codTipo,
        area_max = areaMax,
        financiable= financiable,
        estrato = estrato
    )

    return redirect("listT")

def eliminarTipo(request, codigo):
    tipo = Tipo.objects.get(id_tipo = codigo)
    tipo.delete()    

    return redirect("listT")

def editTipo(request, codigo):
    tipo = Tipo.objects.get(id_tipo = codigo)

    return render(request, "edit/editarTipo.html", {"tipo" : tipo})

def editarTipo(request):
    codigo = request.POST.get("id")
    codTipo = request.POST.get("codTipo")
    areaMax = request.POST.get("areaMax")
    financiable = request.POST.get("financiable")
    estrato = request.POST.get("estrato")

    tipo = Tipo.objects.get(id_tipo = codigo)
    tipo.codigo_tipo = codTipo
    tipo.area_max = areaMax
    tipo.financiable = financiable
    tipo.estrato = estrato
    tipo.save()

    return redirect("listT")

#fin CRUD tipo

#inicio CRUD material construccion

def listMaterial(request):
    materialList = Materialconstruccion.objects.get_queryset().order_by('id_materialconstruccion')
    page = request.GET.get("page", 1)
    
    try:
        paginator = Paginator(materialList, 50)
        materialList = paginator.page(page)
    except:
        raise Http404

    data = {
        "entity" : materialList,
        "paginator" : paginator
    }
    return render(request, "listar/listarMaterial.html", data)

def saveMaterial(request):
    
    return render(request, "save/saveMaterial.html")

def guardarMaterial(request):
    material = request.POST.get("txtMaterial")
    importado = request.POST.get("importado")
    precioUnidad = request.POST.get("precioUnidad")

    material = Materialconstruccion.objects.create(
        nombre_material = material,
        importado= importado,
        precio_unidad = precioUnidad
    )

    return redirect("listaM")

def editMateriales(request, codigo):
    material = Materialconstruccion.objects.get(id_materialconstruccion = codigo)

    return render(request, "edit/editarMaterial.html", {"material" : material})

def editarMateriales(request):
    codigo = request.POST.get("id")
    materiales = request.POST.get("txtMaterial")
    importado = request.POST.get("importado")
    precioUnidad = request.POST.get("precioUnidad")

    material = Materialconstruccion.objects.get(id_materialconstruccion = codigo)
    material.nombre_material = materiales
    material.importado = importado
    material.precio_unidad = precioUnidad
    material.save()

    return redirect("listaM")

def eliminarMaterial(request, codigo):
    material = Materialconstruccion.objects.get(id_materialconstruccion = codigo)
    material.delete()    

    return redirect("listaM")

#fin CRUD material construccion