import qrcode

# Чтение текста из файла
with open('123.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Создание QR-кода
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(text)
qr.make(fit=True)

# Генерация изображения
img = qr.make_image(fill='black', back_color='white')

# Сохранение изображения
img.save("qr_code.png")
print("QR-код сохранён как qr_code.png")
