import hashlib

def haszuj_haslo(haslo):
    hash_md5 = hashlib.md5()
    hash_md5.update(haslo.encode('utf-8'))
    return hash_md5.hexdigest()

def odhaszuj_haslo(zahaszowane_haslo, haslo):
    return haszuj_haslo(haslo) == zahaszowane_haslo

haslo = "316928e0d260556eaccb6627f2ed657b"
zahaszowane_haslo = haszuj_haslo(haslo)
print("Zahaszowane hasło:", zahaszowane_haslo)

print("Poprawność hasła:", odhaszuj_haslo(zahaszowane_haslo, haslo))
