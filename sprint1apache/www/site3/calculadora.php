<html>
<body>
    <h2>Calculadora Aritmética</h2>
        <form method="POST" action="">
        <label for="num1">Número 1:</label>
        <input type="number" step="any" name="num1" required>
        <br><br>
        <label for="num2">Número 2:</label>
        <input type="number" step="any" name="num2" required>
        <br><br>
        <label for="operacion">Operación:</label>
        <select name="operacion" required>
            <option value="suma">Suma</option>
            <option value="resta">Resta</option>
            <option value="multiplicacion">Multiplicación</option>
            <option value="division">División</option>
        </select>
        <br><br>
        <input type="submit" value="Calcular">
    </form>

    <?php
    // Procesamiento del formulario y calculo
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $num1 = $_POST["num1"];
        $num2 = $_POST["num2"];
        $operacion = $_POST["operacion"];
        $resultado = 0;

        // Validación y calculo utilizando switch case
        switch ($operacion) {
            case "suma":
                $resultado = $num1 + $num2;
                echo "<h3>Resultado: $num1 + $num2 = $resultado</h3>";
                break;
            case "resta":
                $resultado = $num1 - $num2;
                echo "<h3>Resultado: $num1 - $num2 = $resultado</h3>";
                break;
            case "multiplicacion":
                $resultado = $num1 * $num2;
                echo "<h3>Resultado: $num1 * $num2 = $resultado</h3>";
                break;
            case "division":
                if ($num2 != 0 || $num1 != 0) {
                    $resultado = $num1 / $num2;
                    echo "<h3>Resultado: $num1 / $num2 = $resultado</h3>";
                } else {
                    echo "<h3>Error: No se puede dividir entre cero</h3>";
                }
                break;
            default:
                echo "<h3>Operación no válida</h3>";
                break;
        }
    }
    ?>

</body>
</html>
