<!--ESTABLECE CONECCION A LA BASE DE DATOS-->
<?php
$db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ejercicios</title>
    <style>
        img{
            width: 100px;
            height: 100px;
        }
    </style>
</head>
<body>

<h1>Conexión establecida</h1>
<?php 
   
   $query = 'SELECT * FROM tLIBROS';
   $result = mysqli_query($db, $query);

   // Verificar si la consulta fue exitosa
   if ($result) {
       // Recorrer los resultados y mostrarlos
       echo "<ul>";
       while ($row = mysqli_fetch_array($result)) {
           // Imprimir el valor del campo 'nombre' de cada fila
         
           echo "<li>id: " . $row['id'] . "</li>";
           echo "<li>Nombre: " . $row['nombre'] . "</li>";
           echo "<li><img src='".$row['url_imagen']."'/></li>";
           echo "<li>Autor: " . $row['autor'] . "</li>";
           echo "<li>numero Paginas: " . $row['numPaginas'] . "</li>";
           echo "<br>";

       }
       echo "</ul>";
   } else {
       // Mostrar mensaje si la consulta falló
       echo "<p>Error en la consulta: " . mysqli_error($db) . "</p>";
   }
   mysqli_close($db);
 ?> 
</body>
</html>