
function validacionC(){

    const $txtCantidad = document.getElementById("txtCantidad").value;
    const $txtProveedor = document.getElementById("txtProveedor");
    const $pagado = document.getElementById("pagado").selectedIndex;
    const $proyecto = document.getElementById("proyecto").selectedIndex;
    const $construccion = document.getElementById("construccion").selectedIndex;    
    let nombre = String($txtProveedor.value).trim();

    if (nombre.length == 0 || nombre == null || /^\s+$/.test(nombre)){
        swal("Proveedor vacio", "...por favor llene este campo!");
        document.getElementById("txtProveedor").style.borderColor="red";
        return false;
    }

    else if($txtCantidad < 0 || $txtCantidad > 100){
        swal("Cantidad no valida", "...por favor llene este campo!");
        document.getElementById("txtCantidad").style.borderColor="red";
        return false;
    }

    else if ($pagado == null || $pagado == 0){
        swal("Pagado vacio", "...por favor llene este campo!");
        document.getElementById("pagado").style.borderColor="red";
        return false;
    }

    else if ($proyecto == null || $proyecto == 0){
        swal("Proyecto vacio", "...por favor llene este campo!");
        document.getElementById("proyecto").style.borderColor="red";
        return false;
    }

    else if ($construccion == null || $construccion == 0){
        swal("Materiales vacio", "...por favor llene este campo!");
        document.getElementById("construccion").style.borderColor="red";
        return false;
    }

    else{        
        swal({
            title: "Guardado!",
            text: "Compra guardada con exito!",
            icon: "success",
          });
        return true;
    }
}

function validarL(form){
    var nombreLider = document.form.txtNombreL.value;
    var apellido = document.form.txtApellido.value;
    var apellidoS = document.form.txtSapellido.value;
    var salario = document.form.salario.value;
    var ciudad = document.form.ciudad.selectedIndex;
    var cargo = document.form.cargo.selectedIndex;
    var clasificacion = document.form.clasificacion.selectedIndex;
    var identificacion = document.form.txtId.value;
    var fechaNacimiento = document.form.fechaNacimiento.value;

    if(nombreLider.length == 0 || nombreLider == null || /^\s+$/.test(nombreLider)){
        swal("Nombre vacio", "...por favor llene este campo!");
        return 0;
    }

    if(apellido.length == 0 || apellido == null || /^\s+$/.test(apellido)){
        swal("Apellido vacio", "...por favor llene este campo!");
        return 0;
    }

    if(apellidoS.length == 0 || apellidoS == null || /^\s+$/.test(apellidoS)){
        swal("Apellido vacio", "...por favor llene este campo!");
        return 0;
    }

    if(salario < 0 || salario > 5000000 || salario.length == 0){
        swal("Salario invalido ó vacio", "...por favor llene este campo!");
        return 0;
    }

    if(ciudad == 0){
        swal("Ciudad vacia", "...por favor llene este campo!");
        return 0;
    }

    if(cargo == 0){
        swal("Cargo vacio", "...por favor llene este campo!");
        return 0;
    }

    if(clasificacion == 0){
        swal("Clasificacion vacio", "...por favor llene este campo!");
        return 0;
    }

    if(identificacion == 0 || nombreLider == null){
        swal("Identificacion vacia", "...por favor llene este campo!");
        return 0;
    }

    if(fechaNacimiento == null || fechaNacimiento == 0){
        swal("Fecha de nacimiento vacio", "...por favor llene este campo!");
        return 0;
    }

    else{        
        swal({
            title: "Guardado!",
            text: "Compra guardada con exito!",
            icon: "success",
          });
          document.formLider.submit();
    }  

}

function validarLe(){
    var nombreLider = document.formLiderE.txtNombreL.value;
    var apellido = document.formLiderE.txtApellido.value;
    var apellidoS = document.formLiderE.txtSapellido.value;
    var salario = document.formLiderE.salario.value;
    var ciudad = document.formLiderE.ciudad.selectedIndex;
    var cargo = document.formLiderE.cargo.selectedIndex;
    var clasificacion = document.formLiderE.clasificacion.selectedIndex;
    var identificacion = document.formLiderE.txtId.value;

    if(nombreLider.length == 0 || nombreLider == null || /^\s+$/.test(nombreLider)){
        swal("Nombre vacio", "...por favor llene este campo!");        
        return 0;
    }

    if(apellido.length == 0 || apellido == null || /^\s+$/.test(apellido)){
        swal("Apellido vacio", "...por favor llene este campo!");
        return 0;
    }

    if(apellidoS.length == 0 || apellidoS == null || /^\s+$/.test(apellidoS)){
        swal("Apellido vacio", "...por favor llene este campo!");
        return 0;
    }

    if(salario < 0 || salario > 5000000 || salario.length == 0){
        swal("Salario invalido ó vacio", "...por favor llene este campo!");
        return 0;
    }

    if(ciudad == 0){
        swal("Ciudad vacia", "...por favor llene este campo!");
        return 0;
    }

    if(cargo == 0){
        swal("Cargo vacio", "...por favor llene este campo!");
        return 0;
    }

    if(clasificacion == 0){
        swal("Clasificacion vacio", "...por favor llene este campo!");
        return 0;
    }

    if(identificacion == 0 || nombreLider == null){
        swal("Identificacion vacia", "...por favor llene este campo!");
        return 0;
    }

    else{
        document.formLiderE.submit();
    }       
     

}


function prueba(a){
    alert(a)
}