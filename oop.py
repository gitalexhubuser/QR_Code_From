import qrcode

class QRCodeGenerator:
    def __init__(self, filename):
        self.filename = filename

    def read_text(self):
        with open(self.filename, 'r', encoding='utf-8') as file:
            return file.read()

    def generate_qr_code(self, text):
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(text)
        qr.make(fit=True)
        return qr.make_image(fill='black', back_color='white')

    def save_qr_code(self, img):
        img.save("qr_code.png")
        print("QR-код сохранён как qr_code.png")

    def create_qr_from_file(self):
        text = self.read_text()
        img = self.generate_qr_code(text)
        self.save_qr_code(img)

# Использование
generator = QRCodeGenerator('123.txt')
generator.create_qr_from_file()
