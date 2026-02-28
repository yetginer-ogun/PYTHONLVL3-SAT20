import string
from password.new_password import generate_password

def test_password_characters():
    """Şifre oluşturulurken yalnızca geçerli karakterlerin kullanıldığını test eder"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Daha güvenli bir doğrulama için uzun bir şifre oluşturuluyor
    for char in password:
        assert char in valid_characters

"""
Aşağıda önerilenlerden birini kullanarak başka bir test yazın. Alternatif olarak, kendi testinizi de oluşturabilirsiniz!
Daha fazla test yazabilirseniz harika olur!

1. Şifrenin uzunluğunun belirtilen uzunlukla eşleşip eşleşmediğini test edin  
2. Arka arkaya oluşturulan iki şifrenin farklı olup olmadığını test edin 
"""

def test_pasword_lenght():
        password = generate_password(15)
        assert password == 15 , "Uzunluk hatalı" 

def test_regenerate_password():
    password1 = generate_password(15)
    password2 = generate_password(15)
    assert password1 != password2 , "Uzunluk hatalı" 

def test_minimum():
    password = generate_password(3)
    assert password == "Çok Kısa", "6 dan kısa şifre oluşturuldu" 