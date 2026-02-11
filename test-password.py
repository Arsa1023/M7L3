import random
import string
def generate_password(length=12):
    """Membuat password acak dengan panjang yang ditentukan."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for i in range(length):
        password += random.choice(characters)
    return password
# Contoh penggunaan
password_length = 12  # Anda dapat memilih panjang password yang diinginkan
print("Password baru Anda:", generate_password(password_length))
import string
from password.password import generate_password
def test_password_characters():
    """Tes untuk memastikan hanya karakter yang diizinkan yang digunakan dalam pembuatan password"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Membuat password yang panjang untuk pengujian yang lebih akurat
    for char in password:
        assert char in valid_characters
"""
Tambahkan satu atau lebih tes dari pilihan berikut. Atau buat tes kamu sendiri.
Akan lebih bagus jika kamu bisa membuat lebih banyak tes!
Tes untuk memastikan panjang password sesuai dengan yang diminta
Tes untuk memastikan dua password yang dibuat berurutan tidak sama
"""