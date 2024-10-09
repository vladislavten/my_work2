from cryptography.fernet import Fernet
import getpass

# Генерация ключа и сохранение его
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Загрузка ключа
def load_key():
    return open("secret.key", "rb").read()

# Шифрование пароля
def encrypt_password(password):
    key = load_key()
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode())
    return encrypted_password

# Дешифрование пароля
def decrypt_password(encrypted_password):
    key = load_key()
    f = Fernet(key)
    decrypted_password = f.decrypt(encrypted_password).decode()
    return decrypted_password

# Пример использования
generate_key()
password = getpass.getpass("Введите пароль: ")
encrypted = encrypt_password(password)
print(f"Encrypted: {encrypted}")

decrypted = decrypt_password(encrypted)
print(f"Decrypted: {decrypted}")
