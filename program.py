# import hashlib


# hashlib.sha224("cos".encode())

# print(f"tak wyglada dla tekstu dla cos"
#       f"= {sha224.hexdigest()}")

# import hashlib
# import sys

# def hash_password(password, hash_algorithm):
#     hash_obj = hashlib.new(hash_algorithm)
#     hash_obj.update(password.encode('utf-8'))
#     return hash_obj.hexdigest()

# def main():
#     if len(sys.argv) != 4:
#         print("Użycie: python program.py <hash> <format-hasha> <wordlista>")
#         sys.exit(1)

#     provided_hash = sys.argv[1]
#     hash_algorithm = sys.argv[2].lower()
#     wordlist_path = sys.argv[3]

#     with open(wordlist_path, 'r', encoding='utf-8') as wordlist_file:
#         for line in wordlist_file:
#             password = line.strip()

#             # Haszowanie hasła zgodnie z podanym formatem
#             hashed_password = hash_password(password, hash_algorithm)

#             # Sprawdzenie, czy wygenerowany hash pasuje do podanego hasha
#             if hashed_password == provided_hash:
#                 print(f"Znalezione hasło: {password}")
#                 sys.exit(0)

#     print("Hasło nie znalezione w wordliście.")
#     sys.exit(1)

# if __name__ == "__main__":
#     main()


import sys

if len(sys.argv) == 4:
    format_haszujacy = sys.argv[1]
    wordlista_sciezka = sys.argv[2]
    hash_do_zlamania = sys.argv[3]

    with open(wordlista_sciezka, 'r') as f:
        lines = f.readlines()

        for l in lines:
            print(l.strip())
else:
    print("Podales za malo argumentow")
