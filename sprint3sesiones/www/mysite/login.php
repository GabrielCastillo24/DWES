<?php
// Conexión a la base de datos
$db = mysqli_connect('127.16.0.2', 'root', '1234', 'mysitedb') or die('Fail');

// Recibir datos del formulario
$email_posted = $_POST['f_email'];
$password_posted = $_POST['f_password'];

// Consulta para verificar el usuario por email
$query = "SELECT id, contraseña FROM tUSUARIO WHERE email = '$email_posted'";
$result = mysqli_query($db, $query) or die('Query error');

// Verificar si se encontró el email
if (mysqli_num_rows($result) > 0) {
    $only_row = mysqli_fetch_array($result);
    $password_hashed = $only_row['contraseña'];

    // Verificar la contraseña usando password_verify
    if (password_verify($password_posted, $password_hashed)) {
        // Iniciar sesión y redirigir a la página principal
        session_start();
        $_SESSION['user_id'] = $only_row['id'];
        header('Location: main.php');
        exit;
    } else {
        // Contraseña incorrecta
        echo '<p>Contraseña incorrecta</p>';
    }
} else {
    // Email no encontrado
    echo '<p>Usuario no encontrado con ese email</p>';
}

// Cerrar conexión a la base de datos
mysqli_close($db);
?>