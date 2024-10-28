<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Detail</title>
    <style>
        img{
            width: 100px;
            height: 100px;
        }
    </style>
</head>
<body>
<!--Coneccion con la base de datos-->
    <?php
    $db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');
    ?>

    <?php
        if (!isset($_GET['libroid'])) {
        die('No se ha especificado un libro');
        }
        $libro_id = $_GET['libroid'];
        $query = 'SELECT * FROM tLIBROS WHERE id='.$libro_id;
        $result = mysqli_query($db, $query) or die('Query error');
        $only_row = mysqli_fetch_array($result);
        echo '<h1>'.$only_row['nombre'].'</h1>';
        echo '<h2>'.$only_row['autor'].'</h2>';
        echo  "<img src='".$only_row['url_imagen']."'/>";
    ?>
<h3>Comentarios:</h3>
<ul>
    <?php
        $query2 = 'SELECT * FROM tCOMENTARIOS WHERE libroId='.$libro_id;
        $result2 = mysqli_query($db, $query2) or die('Query error');
        while ($row = mysqli_fetch_array($result2)) {
        echo '<li>'.$row['comentario'].'</li>';
        }
        mysqli_close($db);
    ?>

    <p>Deja un nuevo comentario:</p>
    <form action="/comment.php" method="post">
        <textarea rows="4" cols="50" name="new_comment"></textarea><br>
        <input type="hidden" name="libroId" value="<?php echo $libro_id;?>">
        <input type="submit" value="Comentar">
    </form>

</ul>
</body>
</html>