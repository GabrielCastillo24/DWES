<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Comment</title>
</head>
<body>
<?php
    // Conectar a la base de datos
    $db = mysqli_connect('172.16.0.2', 'root', '1234', 'mysitedb') or die('Error al conectar a la base de datos');
    
    // Iniciar sesión para verificar si hay un usuario logueado
    session_start();

    // Obtener valores del formulario y escapar datos
    $libro_id = mysqli_real_escape_string($db, $_POST['libroId']);
    $comentario = mysqli_real_escape_string($db, $_POST['new_comment']);
    $fecha = mysqli_real_escape_string($db, $_POST['fechaComentario']);
    
    // Verificar si el usuario está logueado y definir el ID del usuario
    $user_id = 'NULL';
    if (!empty($_SESSION['user_id'])) {
        $user_id = $_SESSION['user_id'];
    }

    // Definir y ejecutar la consulta
    $query = "INSERT INTO tCOMENTARIOS (comentario, libroId, usuarioId, fechaComentario)
              VALUES ('$comentario', $libro_id, $user_id, '$fecha')";
    mysqli_query($db, $query) or die('Error en la inserción');

    // Confirmación de inserción
    echo "<p>Nuevo comentario con ID " . mysqli_insert_id($db) . " añadido</p>";
    echo "<a href='/detail.php?libroid=".$libro_id."'>Volver</a>";

    // Cerrar la conexión
    mysqli_close($db);
    ?>
</body>
</html>