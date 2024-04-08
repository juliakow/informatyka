def ceaser_encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shift_char = chr((ord(char) + shift - 64) % 26 + 65)
            ciphertext += shift_char
        else:
            ciphertext += char

    return ciphertext