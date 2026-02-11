import random
import string

length = int(input("Berapa panjang password yang kau mau?"))

def generate_password(length):
    """Membuat password acak dengan panjang yang ditentukan."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for i in range(length):
        password += random.choice(characters)
    return password
# Contoh penggunaan
password_length = length  # Anda dapat memilih panjang password yang diinginkan
print("Password baru Anda:", generate_password(password_length))