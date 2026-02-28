import random
import string

def generate_password(length=12):
    """Belirtilen uzunlukta rastgele bir şifre oluşturur."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''
    if length < 6:
        return "Şifre en az 6 karakter içermelidir"
    for i in range(length):
        password += random.choice(characters)
    return password

# Kullanım örneği
password_length = 3  # İstediğiniz herhangi bir şifre uzunluğunu seçebilirsiniz
print("Yeni şifreniz:", generate_password(password_length))




