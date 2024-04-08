def decrypt_caesar(ciphertext):
    decrypted_text = ""
    for shift in range(26):
        temp = ""
        for char in ciphertext:
            if char.isalpha():
                if char.islower():
                    shifted = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
                else:
                    shifted = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
                temp += shifted
            else:
                temp += char
        decrypted_text = temp if not decrypted_text else decrypted_text
    return decrypted_text

ciphertext = input("Podaj zaszyfrowany tekst: ")
print("Odszyfrowany tekst:", decrypt_caesar(ciphertext))
