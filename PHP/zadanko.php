<!DOCTYPE html>
<html>
<head>
    <title>Formularz</title>
</head>
<body>
    <form method="post" action="">
        <label for="liczba1">Liczba 1:</label>
        <input type="number" id="liczba1" name="liczba1"><br>
        <label for="liczba2">Liczba 2:</label>
        <input type="number" id="liczba2" name="liczba2"><br>
        <input type="submit" name="submit" value="Oblicz">
    </form>

    <?php
    if (isset($_POST['submit'])) {
        $liczba1 = $_POST['liczba1'];
        $liczba2 = $_POST['liczba2'];

        if ($liczba2 == 0) {2
            echo "Nie można dzielić przez 0.";
        } else {
            $iloraz = $liczba1 / $liczba2;
            echo "Iloraz: " . $iloraz;
        }
    }
    ?>
</body>
</html>
