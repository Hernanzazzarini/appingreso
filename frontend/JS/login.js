function login() {
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    // Puedes realizar la lógica de autenticación aquí

    // Ejemplo de lógica simple de autenticación
    if (username === 'usuario' && password === 'contrasena') {
        alert('Inicio de sesión exitoso');
    } else {
        alert('Error en las credenciales. Inténtalo de nuevo.');
    }
}
