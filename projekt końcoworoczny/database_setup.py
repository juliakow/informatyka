from pymongo import MongoClient

def setup_database():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['voting_app']
    print("Baza danych 'voting_app' została skonfigurowana.")
