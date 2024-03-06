function ingreso() {
    alert("Registro de Ingreso");
}

function egreso() {
    alert("Registro de Egreso");
}

function actualizarFechaHora() {
    var contenedorFechaHora = document.getElementById('fecha-hora');
    var fechaHora = new Date();
    
    // Eliminar la abreviatura de la zona horaria
    var opciones = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric', hour: 'numeric', minute: 'numeric', second: 'numeric' };
    
    var formatoFechaHora = fechaHora.toLocaleDateString('es-ES', opciones);
    contenedorFechaHora.textContent = formatoFechaHora;
}

setInterval(actualizarFechaHora, 1000);

// Agregar la clase 'animate__animated' al contenedor de fecha y hora al cargar la página
document.addEventListener('DOMContentLoaded', function() {
    var contenedorFechaHora = document.getElementById('fecha-hora');
    contenedorFechaHora.classList.add('animate__animated');

    // Llamar a la función para mostrar la fecha y hora al cargar la página
    actualizarFechaHora();
});


