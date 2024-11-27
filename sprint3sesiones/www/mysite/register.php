<?php
// Conexión a la base de datos
$db = mysqli_connect('172.16.0.2', 'root', '1234', 'mysitedb') or die('Error al conectar a la base de datos');

// Recibir datos del formulario
$email = $_POST['email'];
$password = $_POST['password'];
$confirm_password = $_POST['confirm_password'];

// Validación de campos vacíos
if (empty($email) || empty($password) || empty($confirm_password)) {
    echo '<p>Todos los campos son obligatorios.</p>';
    exit;
}

// Comprobar si las contraseñas coinciden
if ($password !== $confirm_password) {
    echo '<p>Las contraseñas no coinciden.</p>';
    exit;
}

// Comprobar si el correo ya existe en la base de datos
$query = "SELECT id FROM tUSUARIO WHERE email = '$email'";
$result = mysqli_query($db, $query);

if (mysqli_num_rows($result) > 0) {
    echo '<p>El correo ya está registrado.</p>';
    exit;
}

// Hash de la contraseña
$password_has = password_hash($password, PASSWORD_DEFAULT);

// Insertar el nuevo usuario en la base de datos
$query = "INSERT INTO tUSUARIO (email, contraseña) VALUES ('$email', '$password_has')";
if (mysqli_query($db, $query)) {
    // Redirigir al usuario a la página principal después del registro exitoso
    header('Location: main.php');
    exit;
} else {
    echo '<p>Error al registrar el usuario. Inténtalo de nuevo.</p>';
}

mysqli_close($db);
?>