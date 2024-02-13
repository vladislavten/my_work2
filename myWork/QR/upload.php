<?php
$targetDir = "D:\Python_Basic\myWork\QR\images";  // Путь к директории для сохранения файла
$targetFile = $targetDir . basename($_FILES["fileToUpload"]["name"]);  // Имя файла с путем

// Проверка, что файл был успешно загружен
if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $targetFile)) {
    echo "Файл ". basename( $_FILES["fileToUpload"]["name"]). " успешно загружен.";
} else {
    echo "Ошибка при загрузке файла.";
}
?>
