from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

def generate_ecc_keys():
    """Generuje parę kluczy ECC i zapisuje je do plików."""
    private_key = ec.generate_private_key(ec.SECP384R1())
    public_key = private_key.public_key()

    serialize_key(private_key, "private_key.pem")
    serialize_key(public_key, "public_key.pem")

    return private_key, public_key

def serialize_key(key, filename):
    """Serializuje klucz do formatu PEM i zapisuje do pliku."""
    pem = key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    ) if isinstance(key, ec.EllipticCurvePrivateKey) else key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    with open(filename, "wb") as f:
        f.write(pem)

def encrypt_message(public_key, message):
    """Szyfruje wiadomość za pomocą klucza publicznego."""
    return public_key.encrypt(
        message,
        ec.ECDH()
    )

def decrypt_message(private_key, ciphertext):
    """Deszyfruje wiadomość za pomocą klucza prywatnego."""
    return private_key.decrypt(
        ciphertext,
        ec.ECDH()
    )

def main():
    # Generowanie kluczy
    private_key, public_key = generate_ecc_keys()

    # Szyfrowanie wiadomości    
    message = b = "Tajna wiadomość"
    ciphertext = encrypt_message(public_key, message)

    # Deszyfrowanie wiadomości
    original_message = decrypt_message(private_key, ciphertext)

    print("Odszyfrowana wiadomość:", original_message.decode())

if __name__ == "__main__":
    main()
