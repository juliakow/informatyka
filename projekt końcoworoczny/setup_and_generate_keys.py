import sys
from database_setup import setup_database
from generateRSAKeys import generate_RSA_keys

def main():
    # Konfiguracja bazy danych
    print("Konfiguracja bazy danych...")
    setup_database()

    # Generowanie kluczy RSA
    print("\nGenerowanie kluczy RSA...")
    generate_RSA_keys()

if __name__ == "__main__":
    main()
