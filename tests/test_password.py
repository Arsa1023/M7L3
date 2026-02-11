import string
from password.password import generate_password


def test_password_characters():
    """Tes untuk memastikan hanya karakter yang diizinkan yang digunakan dalam pembuatan password"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)

    for char in password:
        assert char in valid_characters


def test_password_length():
    """Tes untuk memastikan panjang password sesuai yang diminta"""
    length = 12
    password = generate_password(length)
    assert len(password) == length


def test_passwords_are_different():
    """Tes untuk memastikan dua password yang dibuat tidak sama"""
    password1 = generate_password(12)
    password2 = generate_password(12)

    assert password1 != password2
