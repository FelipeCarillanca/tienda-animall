const nombre = document.getElementById("myname");
const apellidos = document.getElementById("surname");
const correo = document.getElementById("email");
const celular = document.getElementById("mobile");
const contraseña = document.getElementById("password");
const repetircontraseña = document.getElementById("repeatpassword");
const terminosYcondiciones = document.getElementById("termsAndConditions");
const form = document.getElementById("form");
const listInputs = document.querySelectorAll(".form-input");

form.addEventListener("submit", (e) => {
    e.preventDefault();
    let condicion = validacionForm();
    if (condicion) {
        enviarformulario();
    }
    
});

function validacionForm() {
    let condicion = true;
    listInputs.forEach((element) => {
        element.lastElementChild.innerHTML = "";
    });

    if(nombre.value.length < 1 || nombre.value.trim() == "") {
        mostrarMensajeError("myname", "Nombre no valido*");
        let condicion = false;
    }
    if(apellidos.value.length < 1 || apellidos.value.trim() ==""){
        mostrarMensajeError("surname", "Apellido no valido*");
        let condicion = false;
    }
    if(correo.value.length < 1 || correo.value.trim() ==""){
        mostrarMensajeError("email", "correo no valido*");
        let condicion = false;
    }
    if(celular.value.length != 9 || celular.value.trim() ==""){
        mostrarMensajeError("mobile", "celular no valido*");
        condicion = false;
    }
    if(contraseña.value.length < 1 || contraseña.value.trim() ==""){
        mostrarMensajeError("password", "contraseña no valido*");
        let condicion = false;
    }
    if(repetircontraseña.value != contraseña.value){
        mostrarMensajeError("repeatpassword", "contraseña error*");
        let condicion = false;
    }
    if (!terminosYcondiciones.checked) {
        mostrarMensajeError("termsAndConditions", "Acepte*");
        let condicion = false;
    } else{
        mostrarMensajeError("termsAndConditions", "");
        let condicion = true;
    }
    return condicion;
}

function mostrarMensajeError(claseInput,mensaje) {
    let elemento = document.querySelector(`.${claseInput}`);
    elemento.lastElementChild.innerHTML = mensaje;
}

function enviarformulario() {
    form.reset();
    form.lastElementChild.innerHTML = "Listo";
}





