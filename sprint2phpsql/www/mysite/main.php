<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ejercicios</title>
</head>
<body>
<!--ESTABLECE CONECCION A LA BASE DE DATOS-->
<?php
$db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');
?>
<h1>Conexión establecida</h1>
<?php 
 // Lanzar una query 
 $query = 'SELECT * FROM tCanciones'; 
 mysqli_query($db, $query) or die('Query error'); 
 ?> 
</body>
</html>