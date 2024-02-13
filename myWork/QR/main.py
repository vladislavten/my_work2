import qrcode

# URL для создания QR-кода
url = "Http://www.anpz.kzkjhdsfkjhsdfkjhsdfakjhfsdakjhsdafhkjsfdahkj"

# Создание объекта QRCode
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)

# Добавление данных в объект QRCode
qr.add_data(url)
qr.make(fit=True)

# Создание изображения QR-кода
qr_img = qr.make_image(fill_color="black", back_color="white")

# Сохранение изображения в файл
qr_img.save("qr_code.png")

print("QR-код успешно создан и сохранен в файл 'qr_code.png'.")
