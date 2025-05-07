from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton,
    QFileDialog, QMessageBox, QSpinBox
)
from PyQt6.QtGui import QPixmap, QDragEnterEvent, QDropEvent
from PyQt6.QtCore import Qt
from PIL import Image
import numpy as np
import sys


def encrypt_image(img_path, key):
    img = Image.open(img_path)
    pixels = np.array(img)

    pixels = 255 - pixels
    pixels = pixels ^ key
    pixels = np.flipud(pixels)
    pixels = np.rot90(pixels)

    encrypted = Image.fromarray(pixels)
    encrypted_path = "Encrypted_image.png"
    encrypted.save(encrypted_path)
    return encrypted_path


def decrypt_image(img_path, key):
    img = Image.open(img_path)
    pixels = np.array(img)

    pixels = pixels ^ key
    pixels = np.rot90(pixels, k=3)
    pixels = np.flipud(pixels)
    pixels = 255 - pixels

    decrypted = Image.fromarray(pixels)
    decrypted_path = "Decrypted_image.png"
    decrypted.save(decrypted_path)
    return decrypted_path


class ImageEncryptor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Encryptor / Decryptor")
        self.setGeometry(100, 100, 400, 300)
        self.setAcceptDrops(True)  # Enable drag-and-drop

        self.selected_file = None

        self.layout = QVBoxLayout()

        self.label = QLabel("Choose an image to encrypt or decrypt\n(Drag & drop supported)")
        self.layout.addWidget(self.label)

        self.key_input = QSpinBox()
        self.key_input.setRange(1, 255)
        self.layout.addWidget(self.key_input)

        self.encrypt_btn = QPushButton("Encrypt Image")
        self.decrypt_btn = QPushButton("Decrypt Image")
        self.layout.addWidget(self.encrypt_btn)
        self.layout.addWidget(self.decrypt_btn)

        self.setLayout(self.layout)

        self.encrypt_btn.clicked.connect(self.encrypt_handler)
        self.decrypt_btn.clicked.connect(self.decrypt_handler)

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        urls = event.mimeData().urls()
        if urls:
            file_path = urls[0].toLocalFile()
            self.selected_file = file_path
            self.label.setText(f"Selected file: {file_path}")

    def get_key(self):
        try:
            return int(self.key_input.text())
        except ValueError:
            QMessageBox.warning(self, "Invalid Key", "Please enter a valid numeric key.")
            return None

    def encrypt_handler(self):
        file_path = self.selected_file or QFileDialog.getOpenFileName(self, "Select Image")[0]
        if file_path:
            key = self.get_key()
            if key is not None:
                out_path = encrypt_image(file_path, key)
                QMessageBox.information(self, "Success", f"Encrypted image saved as: {out_path}")

    def decrypt_handler(self):
        file_path = self.selected_file or QFileDialog.getOpenFileName(self, "Select Encrypted Image")[0]
        if file_path:
            key = self.get_key()
            if key is not None:
                out_path = decrypt_image(file_path, key)
                QMessageBox.information(self, "Success", f"Decrypted image saved as: {out_path}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ImageEncryptor()
    window.show()
    sys.exit(app.exec())
