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
password_length = int(input("Enter how many word do you want?"))  # Anda dapat memilih panjang password yang diinginkan
print("Password baru Anda:", generate_password(password_length))