# 🖼️ PyQt6 Image Encryptor / Decryptor

A simple PyQt6 desktop application that allows users to encrypt and decrypt images using a numeric key. The app supports drag-and-drop image selection, manual file browsing, and real-time key entry.

---

## 🚀 Features

- 🔐 **Image Encryption & Decryption**
- 🧮 **User-defined Numeric Key**
- 🖱️ **Drag-and-Drop Image Support**
- 📁 **File Dialog for Manual Selection**
- ⚡ **Simple and Responsive UI**

---

## 📸 How It Works

1. Select or drag-and-drop an image file (PNG, JPG, etc.).
2. Enter a numeric encryption key (e.g., `123`).
3. Click `Encrypt Image` or `Decrypt Image`.
4. Encrypted/decrypted image will be saved in the working directory.

Encryption uses:
- Color inversion
- Bitwise XOR with the key
- Vertical flipping
- 90-degree rotation

Decryption reverses these operations.

---

## 🧑‍💻 Requirements

- Python 3.7+
- [PyQt6](https://pypi.org/project/PyQt6/)
- [Pillow](https://pypi.org/project/Pillow/)
- [NumPy](https://pypi.org/project/numpy/)

Install dependencies with:

```bash
pip install PyQt6 Pillow numpy
