<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Comment</title>
</head>
<body>
    <?php
    $db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');
    ?>

<?php
    // Obtener valores del formulario
    $libro_id = $_POST['libroId'];
    $comentario = $_POST['new_comment'];
    $fecha = $_POST['fechaComentario'];
    // Definir y ejecutar la consulta
    $query = "INSERT INTO tCOMENTARIOS(comentario, libroId, usuarioId, fechaComentario)
              VALUES ('".$comentario."', ".$libro_id.", NULL, '".$fecha."')";
    mysqli_query($db, $query) or die('Error en la inserción');

    // Confirmación de inserción
    echo "<p>Nuevo comentario ";
    echo mysqli_insert_id($db);
    echo " añadido</p>";

    echo "<a href='/detail.php?libroid=".$libro_id."'>Volver</a>";

    // Cerrar la conexión
    mysqli_close($db);
?>
</body>
</html>