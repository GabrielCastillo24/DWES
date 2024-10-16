<html>
<body>
<h1>Jubilación</h1>
<?php
  function edad_en_10_años($edad) {
  return $edad+10;
  }
  $edad2 = $_GET["edad"];
  if (edad_en_10_años($edad2) > 65) {
  echo "En ".(65-$edad2)." años tendrás edad de jubilación";
  } else {
  echo "¡Disfruta de tu tiempo!";
  }
  ?>
 </body>
</html>
